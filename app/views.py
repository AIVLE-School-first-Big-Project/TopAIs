from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
<<<<<<< HEAD
from app.email_auth import EmailAuthView
from app.forms import CompanyForm, AgencyForm
=======
from app.forms import CompanyRegistrationForm, AgencyRegistrationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
>>>>>>> a1d5a3ac2992ca3467300f3f2de7f02066ba91d2


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
