from django.db import models


# Create your models here.
class PostNotice(models.Model):
    content = models.CharField(max_length=500)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'post_notice'
