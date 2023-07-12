from django.db import models

# Create your models here.


class Weather(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    detailing = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now=True)
    response = models.JSONField()
