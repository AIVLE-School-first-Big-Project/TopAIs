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

# def login(request):
#     return render(request, 'app/login.html')

# def signup_selecttype(request):
#     return render(request, 'app/signup_selecttype.html')

# def signup_com(request):
#     return render(request, 'app/signup_com.html')

# def signup_official(request):
#     return render(request, 'app/signup_official.html')

# def service_writework(request):
#     return render(request, 'app/service_writework.html')

# def board_list(request):
#     return render(request, 'app/board_list.html')

# def map(request):
#     return render(request, 'app/map.html')

# def pwchange(request):
#     return render(request, 'app/pwchange.html')

# def mypage(request):
#     return render(request, 'app/mypage.html')
