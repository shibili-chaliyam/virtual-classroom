from django.db import models

# Create your models here.
class VideoConferencing(models.Model):
    link = models.CharField(max_length=50)
    semester = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'video_conferencing'

