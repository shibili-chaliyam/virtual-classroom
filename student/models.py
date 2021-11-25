from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    course = models.CharField(max_length=55)
    semester = models.IntegerField()
    address = models.CharField(max_length=50)
    contact = models.IntegerField()
    status = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'student'


# class RegisterDep(models.Model):
#     name = models.CharField(max_length=50)
#     info = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'register_dep'
