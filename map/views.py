from distutils.command.build import build
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model

import json

from .models import Facility, Building

from accounts.views import is_company, is_Agency, is_writable

# Create your views here.

login_url = '/accounts/login'


@csrf_exempt
@login_required(login_url=login_url)
@user_passes_test(is_writable)
def service_coolRoof(request):
    print(get_user_model().is_writeable)
    building = Building.objects.filter(city='부산광역시').values(
        "latitude", "longitude", "city", "county", "district", "number1", "number2")

    areas = {}
    for i in range(len(building)):
        areas[str(i)] = building[i]

    return render(request, 'service_coolRoof.html', context={'areas': areas})


@csrf_exempt
@login_required(login_url=login_url)
@user_passes_test(is_writable)
def service_roadLine(request):
    return render(request, 'service_roadLine.html')
