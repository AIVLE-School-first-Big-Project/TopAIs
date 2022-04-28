from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from app.forms import CompanyRegistrationForm, AgencyRegistrationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def albums(request):
    return render(request, 'app/albums.html')


def blog(request):
    return render(request, 'app/blog.html')


def elements(request):
    return render(request, 'app/elements.html')


def event(request):
    return render(request, 'app/event.html')


def index(request):
    return render(request, 'app/index.html')
