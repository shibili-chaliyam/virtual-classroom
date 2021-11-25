from django.db import models

# Create your models here.
class InternalTimeTable(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    ending_time = models.TimeField()
    subject = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'internal_time_table'

