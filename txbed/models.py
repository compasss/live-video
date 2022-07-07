from django.db import models

# Create your models here.


class AohsFile(models.Model):
    def __str__(self):
        return self.file_name
    id = models.BigAutoField(primary_key=True)
    file_name = models.CharField(max_length=200)
    url = models.CharField(max_length=512)
    content_type = models.CharField(max_length=64, blank=True)
    extra = models.JSONField()
