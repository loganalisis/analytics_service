from django.db import models

class LogAnalytics(models.Model):
    file_name = models.CharField(max_length=255)
    blob_url = models.URLField()
    error_count = models.IntegerField(default=0)
    requests_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
