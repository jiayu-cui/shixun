from django.db import models

# Create your models here.

class Auther(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        db_table='auther'


class Book(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    auther = models.ForeignKey(Auther,models.DO_NOTHING,blank=True, null=True)
    img = models.CharField(max_length=100,blank=True, null=True)
    class Meta:
        db_table='book'








