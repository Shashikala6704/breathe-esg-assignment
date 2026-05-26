from django.urls import path
from .views import CSVUploadView, ActivityListView, update_activity_status

urlpatterns = [
    path('upload/', CSVUploadView.as_view(), name='upload'),
    path('activities/', ActivityListView.as_view(), name='activities'),
    path('activities/<int:activity_id>/status/', update_activity_status, name='update_activity_status'),
]