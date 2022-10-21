from django.db import models


# Create your models here.
class Device(models.Model):
  username = models.CharField(max_length=255)
  deviceID = models.IntegerField()
  region = models.CharField(max_length=255)
  mqttuser = models.CharField(max_length=255)
  mqttpass = models.CharField(max_length=255)

# class UserRegister(models.Model):
#   email = models.EmailField()
#   password = models.CharField(max_length=255)
#   first_name = models.CharField(max_length=255)
#   last_name = models.CharField(max_length=255)

class Nordpool(models.Model):
  Date = models.DateTimeField()
  Hour = models.CharField(max_length=255)
  SYS = models.FloatField(max_length=255)
  SE1 = models.FloatField(max_length=255)
  SE2 = models.FloatField(max_length=255)
  SE3 = models.FloatField(max_length=255)
  SE4 = models.FloatField(max_length=255)
  FI = models.FloatField(max_length=255)
  DK1 = models.FloatField(max_length=255)
  DK2 = models.FloatField(max_length=255)
  Oslo = models.FloatField(max_length=255)
  Kr_sand = models.FloatField(max_length=255)
  Bergen = models.FloatField(max_length=255)
  Molde = models.FloatField(max_length=255)
  TR_heim = models.FloatField(max_length=255)
  Tromso = models.FloatField(max_length=255)
  EE = models.FloatField(max_length=255)
  LV = models.FloatField(max_length=255)
  LT = models.FloatField(max_length=255)
  AT = models.FloatField(max_length=255)
  BE = models.FloatField(max_length=255)
  DE_LU = models.FloatField(max_length=255)
  FR = models.FloatField(max_length=255)
  NL = models.FloatField(max_length=255)