from django.db import models

class UploadSession(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='uploads/')
    original_filename = models.CharField(max_length=255)

    def __str__(self):
        return self.original_filename

class AnalysisResult(models.Model):
    session = models.OneToOneField(UploadSession, on_delete=models.CASCADE)
    mean = models.JSONField()
    mode = models.JSONField()
    value_counts = models.JSONField()
    null_counts = models.JSONField()
    dtypes = models.JSONField()
    duplicates_removed = models.IntegerField()

    def __str__(self):
        return f'Analysis for {self.session.original_filename}'
