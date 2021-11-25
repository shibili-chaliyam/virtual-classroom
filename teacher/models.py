from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    qualification = models.CharField(max_length=55)
    subject = models.CharField(max_length=50)
    mob_no = models.IntegerField()
    dep_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'teacher'

