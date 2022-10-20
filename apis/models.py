from django.db import models

# Create your models here.


class HistoricalInterestDataFrame(models.Model):
    date = models.DateField()
    egypt = models.IntegerField()
    class Meta:
        managed = False




class InterestByRegion(models.Model):
    
    class Meta:
        managed = False
