from django.db import models
from datetime import datetime

from django.db.models import base

GENDER = (
    ('female','FEMALE'),
    ('male','MALE'),
)


class Diabetes(models.Model):
    Patient_name = models.CharField(max_length = 200, blank =False)
    Gender = models.CharField(max_length = 8, choices= GENDER)
    Pregnancy = models.CharField(max_length=5,blank=True, null=True)
    Glucose = models.CharField(max_length=50, blank=False)
    Blood_Pressure = models.CharField(max_length=50, blank=False)
    Skin_thickness = models.CharField(max_length=50, blank=False)
    Insulin = models.CharField(max_length=50, blank=False)
    BMI = models.FloatField(max_length=50, blank=False)
    Diabetes_Pedigree_Function = models.FloatField(max_length=50, blank=False)
    Age = models.IntegerField(blank=False)
    Date = models.DateTimeField(default=datetime.now, blank=True)
    Probablity_percent = models.CharField(max_length = 50, blank =True)
    def __str__(self):
        return self.Patient_name

