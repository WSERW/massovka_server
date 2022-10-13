from calendar import month
from pydoc import plain
from django.db import models

# Create your models here.

class Shop(models.Model):
    name = models.CharField(max_length=255)

class Report(models.Model):
    shop = models.ForeignKey(Shop, related_name='reports', on_delete=models.SET_NULL,null=True)
    month = models.DateField()
    planTO = models.DecimalField(max_digits=12,decimal_places=2)
    planTraffic = models.IntegerField()
    planNum = models.IntegerField()
    factTO = models.DecimalField(max_digits=12,decimal_places=2)
    factTraffic = models.IntegerField()
    factNum = models.IntegerField()