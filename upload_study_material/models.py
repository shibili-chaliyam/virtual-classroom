from django.db import models

# Create your models here.
class UploadStudyMaterial(models.Model):
    semester = models.IntegerField()
    material = models.CharField(max_length=55)
    teacher_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'upload_study_material'

