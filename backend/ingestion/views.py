import pandas as pd

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import (
    SourceSystem,
    IngestionBatch,
    RawRecord,
    NormalizedActivity
)


class CSVUploadView(APIView):

    def post(self, request):

        file = request.FILES.get('file')
        source_type = request.data.get('source_type')

        if not file:
            return Response(
                {"error": "No file uploaded"},
                status=status.HTTP_400_BAD_REQUEST
            )

        df = pd.read_csv(file)

        source_system, _ = SourceSystem.objects.get_or_create(
            name=source_type,
            source_type=source_type
        )

        batch = IngestionBatch.objects.create(
            source_system=source_system,
            file_name=file.name
        )

        created_rows = 0

        for index, row in df.iterrows():

            raw_record = RawRecord.objects.create(
                batch=batch,
                row_number=index + 1,
                raw_payload=row.to_dict()
            )

            quantity = row.get('Quantity', 0)

            suspicious_reason = ""

            if pd.isna(quantity) or quantity == 0:
                suspicious_reason = "Missing quantity"

            activity = NormalizedActivity.objects.create(
                raw_record=raw_record,
                source_type=source_type,
                scope='Scope 1',
                activity_type='Fuel Consumption',
                quantity=quantity if not pd.isna(quantity) else 0,
                original_unit=row.get('Unit', ''),
                normalized_quantity=quantity if not pd.isna(quantity) else 0,
                normalized_unit=row.get('Unit', ''),
                status='suspicious' if suspicious_reason else 'pending',
                suspicious_reason=suspicious_reason
            )

            created_rows += 1

        return Response({
            "message": "File uploaded successfully",
            "rows_created": created_rows
        })
from rest_framework.generics import ListAPIView
from .serializers import NormalizedActivitySerializer


class ActivityListView(ListAPIView):
    queryset = NormalizedActivity.objects.all().order_by('-created_at')
    serializer_class = NormalizedActivitySerializer

from rest_framework.decorators import api_view


@api_view(['POST'])
def update_activity_status(request, activity_id):
    try:
        activity = NormalizedActivity.objects.get(id=activity_id)
    except NormalizedActivity.DoesNotExist:
        return Response({"error": "Activity not found"}, status=404)

    new_status = request.data.get("status")

    if new_status not in ["approved", "rejected", "pending", "suspicious"]:
        return Response({"error": "Invalid status"}, status=400)

    activity.status = new_status
    activity.save()

    return Response({
        "message": "Status updated successfully",
        "id": activity.id,
        "status": activity.status
    })