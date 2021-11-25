from django.db import models

# Create your models here.
class SetTimeTable(models.Model):
    table_id = models.AutoField(primary_key=True)
    teacher_name = models.CharField(max_length=20)
    day = models.CharField(max_length=10)
    period = models.IntegerField()
    subject = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'set_time_table'

