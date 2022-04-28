from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout, authenticate
from .forms import AuthenticationForm, AgencyRegistrationForm, CompanyRegistrationForm


def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
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
            return redirect('login')

        else:
            context['form'] = form

    return render(request, 'signup_official.html', context)


@csrf_exempt
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
            if user:
                login(request, user)
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                return redirect('index')
        else:
            context['form'] = form
    return render(request, 'login.html', context)


def logout_accounts(request):
    logout(request)
    return redirect('index')
