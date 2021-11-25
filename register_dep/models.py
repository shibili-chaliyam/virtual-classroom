from django.db import models

# Create your models here.
class RegisterDep(models.Model):
    name = models.CharField(max_length=50)
    info = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'register_dep'

