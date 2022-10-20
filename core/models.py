from django.db import models


# Create your models here.
class Device(models.Model):
  deviceID = models.IntegerField()
  region = models.CharField(max_length=255)
  setting = models.CharField(max_length=255)
  mqttuser = models.CharField(max_length=255)
  mqttpass = models.CharField(max_length=255)