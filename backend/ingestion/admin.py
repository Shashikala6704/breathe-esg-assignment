from django.contrib import admin
from .models import SourceSystem, IngestionBatch, RawRecord, NormalizedActivity

admin.site.register(SourceSystem)
admin.site.register(IngestionBatch)
admin.site.register(RawRecord)
admin.site.register(NormalizedActivity)