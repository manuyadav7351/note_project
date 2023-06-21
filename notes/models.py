from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = RichTextField()
    audio = models.FileField(upload_to='audio/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)

    def __str__(self):
        return self.title
