from django.db import models

# Create your models here.
class Login(models.Model):
    login_id = models.AutoField(primary_key=True)
    uid = models.IntegerField()
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'login'


