from django.db import models

# Create your models here.


class VideoHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    create_date = models.DateTimeField('create time')
    file_name = models.CharField(max_length=256)
    delete = models.BooleanField(False)
