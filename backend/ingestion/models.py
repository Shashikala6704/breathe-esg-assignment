from django.db import models


class SourceSystem(models.Model):
    SOURCE_CHOICES = [
        ('SAP', 'SAP'),
        ('UTILITY', 'Utility'),
        ('TRAVEL', 'Travel'),
    ]

    name = models.CharField(max_length=100)
    source_type = models.CharField(max_length=20, choices=SOURCE_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.source_type})"


class IngestionBatch(models.Model):
    source_system = models.ForeignKey(SourceSystem, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    status = models.CharField(max_length=50, default='completed')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name


class RawRecord(models.Model):
    batch = models.ForeignKey(IngestionBatch, on_delete=models.CASCADE)
    row_number = models.IntegerField()
    raw_payload = models.JSONField()
    status = models.CharField(max_length=50, default='parsed')
    error_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Row {self.row_number}"


class NormalizedActivity(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('suspicious', 'Suspicious'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    raw_record = models.ForeignKey(RawRecord, on_delete=models.CASCADE)
    source_type = models.CharField(max_length=20)
    scope = models.CharField(max_length=20)
    activity_type = models.CharField(max_length=100)
    activity_date = models.DateField(null=True, blank=True)
    site_code = models.CharField(max_length=100, blank=True, null=True)

    quantity = models.FloatField(null=True, blank=True)
    original_unit = models.CharField(max_length=50, blank=True, null=True)
    normalized_quantity = models.FloatField(null=True, blank=True)
    normalized_unit = models.CharField(max_length=50, blank=True, null=True)

    emission_factor = models.FloatField(default=0)
    co2e = models.FloatField(default=0)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    suspicious_reason = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.source_type} - {self.activity_type}"