from django.db import models
from register_dep.models import RegisterDep
# Create your models here.
class Hod(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=55)
    qualification = models.CharField(max_length=50)
    dep_id = models.CharField(max_length=50)
    # dep=models.ForeignKey(RegisterDep,to_field='id',on_delete=models.CASCADE)
    mobile = models.IntegerField(max_length=10)
    # status = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'hod'

