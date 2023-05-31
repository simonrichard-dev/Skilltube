from django.db import models
import uuid

# Create your models here.

class Video(models.Model):
    caption = models.CharField(max_length=255)
    video_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    video = models.FileField(upload_to='main/%y')


    def __str__(self):
        return self.caption


class Thumbnail(models.Model):
    thumbnail_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    thumbnail_path = models.CharField(max_length=255)

    def __str__(self):
        return self.thumbnail_path
