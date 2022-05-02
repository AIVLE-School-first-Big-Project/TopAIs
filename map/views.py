from distutils.command.build import build
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
import json

from .models import Facility, Building

# Create your views here.


def service_coolRoof(request):
    building = Building.objects.filter(city='부산광역시').values(
        "latitude", "longitude", "city", "county", "district", "number1", "number2")
    
    areas = {}
    for i in range(len(building)):
        areas[str(i)] = building[i]
    
    return render(request, 'service_coolRoof.html', context={'areas': areas})


def service_roadLine(request):
    return render(request, 'service_roadLine.html')