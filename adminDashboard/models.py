from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vehicle(models.Model):
    vehicle_no = models.IntegerField()
    engine_no = models.IntegerField()
    chassis_no = models.IntegerField()
    Fuel = models.CharField(max_length=10)
    Fuel_cap = models.IntegerField(null=False)
    Manufacturer = models.CharField(max_length=100)
    Model = models.CharField(max_length=200,null=False)
    RC = models.DateField(null=False)
    Insurance = models.DateField()

    def __int__(self):
        return self.vehicle_no

class Device(models.Model):
    device_id = models.IntegerField()
    hardware_ver = models.CharField(max_length=200)
    software_ver = models.CharField(max_length=200)
    model = models.CharField(max_length=200)

    def __int__(self):
        return self.model

class Person(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    blood_group = models.CharField(max_length=10)
    licence_no = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=100)
    vheicleId = models.ManyToManyField(Vehicle)
    deviceId = models.ManyToManyField(Device)
    personId = models.ManyToManyField(Person)
    userId = models.ManyToManyField(User)
