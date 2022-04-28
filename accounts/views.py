from email import message
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from accounts.email_auth import EmailAuthView
from .forms import AuthenticationForm, AgencyRegistrationForm, CompanyRegistrationForm


def signup(request):
    return render(request, 'signup.html')


@csrf_exempt
def signup_company(request):
    # user가 로그인 상태시 main으로 리다이렉트
    if request.user.is_authenticated:
        return redirect('index')

    context = {}
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user_type = 'Company'
            form.save()
            EmailAuthView.post(request, form)
            messages.info(request, '이메일 인증 후 로그인해주세요.')
            return redirect('login')
        else:
            context['form'] = form

    return render(request, 'signup_company.html', context)


@csrf_exempt
def signup_official(request):
    # user가 로그인 상태시 main으로 리다이렉트
    if request.user.is_authenticated:
        return redirect('index')

    context = {}
    if request.method == 'POST':
        form = AgencyRegistrationForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user_type = 'Agency'
            form.save()
            EmailAuthView.post(request, form)
            messages.info(request, '이메일 인증 후 로그인해주세요.')
            return redirect('login')
        else:
            context['form'] = form

    return render(request, 'signup_official.html', context)


def login_accounts(request):
    if request.user.is_authenticated:
        return redirect('index')

    context = {}
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user_id = request.POST['user_id']
            password = request.POST['password']
            user = authenticate(user_id=user_id, password=password)
            aa = user.email_auth
            # request.dd
            try:
                if user.email_auth is False:
                    messages.info(request, '이메일 인증 후 로그인해주세요.')
                else:
                    login(request, user)
                    return redirect('index')
            except: pass
        else:
            context['form'] = form
    return render(request, 'login.html', context)


def logout_accounts(request):
    logout(request)
    return redirect('index')
