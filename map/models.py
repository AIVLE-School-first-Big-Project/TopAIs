from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

from board.models import Board


# Create your models here.

class Facility(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    area = models.FloatField()
    facility_type = models.CharField(max_length=32, null=True)

    class Meta:
        db_table = 'Facility'


class Building(Facility, models.Model):
    name = models.CharField(max_length=30, null=True)
    city = models.CharField(max_length=20)  # 시
    county = models.CharField(max_length=20)  # 군
    district = models.CharField(max_length=20)  # 구
    number1 = models.CharField(max_length=20)  # 지번1
    number2 = models.CharField(max_length=20)  # 지번2

    class Meta:
        db_table = 'Building'


class Business(models.Model):
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Business'
