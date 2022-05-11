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
    name = models.CharField(max_length=32, null=True)
    city = models.CharField(max_length=32)  # 시
    county = models.CharField(max_length=32)  # 군
    district = models.CharField(max_length=32)  # 구
    number1 = models.CharField(max_length=32)  # 지번1
    number2 = models.CharField(max_length=32)  # 지번2
    electro_201608 = models.FloatField(default=0)  # 2016년 8월 전기료
    electro_201708 = models.FloatField(default=0)  # 2016년 8월 전기료
    electro_201808 = models.FloatField(default=0)  # 2016년 8월 전기료
    electro_201908 = models.FloatField(default=0)  # 2016년 8월 전기료
    electro_202008 = models.FloatField(default=0)  # 2016년 8월 전기료
    electro_202108 = models.FloatField(default=0)  # 2016년 8월 전기료
    etcPurps = models.CharField(max_length=64, null=True)  # 건물 용도
    newPlatPlc = models.CharField(max_length=64, null=True)  # 도로명 주소

    class Meta:
        db_table = 'Building'


class Business(models.Model):
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Business'
