from django.db import models

# Create your models here.


class VideoHistory(models.Model):
    create_date = models.DateTimeField('create time')
    file_name = models.CharField(max_length=256)
    delete = models.BooleanField(False)
