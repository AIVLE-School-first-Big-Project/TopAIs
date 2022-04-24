from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from app.forms import CompanyRegistrationForm, AgencyRegistrationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate


def albums(request):
    return render(request, 'app/albums.html')


def blog(request):
    return render(request, 'app/blog.html')


def service_coolroof(request):
    return render(request, 'app/service_coolroof.html')


def service_roadline(request):
    return render(request, 'app/service_roadline.html')


def elements(request):
    return render(request, 'app/elements.html')


def event(request):
    return render(request, 'app/event.html')


def index(request):
    return render(request, 'app/index.html')


def signup_selecttype(request):
    # user가 로그인 상태시 Main으로 다이렉트
    user = request.user
    if user.is_authenticated:
        return redirect('index')
    return render(request, 'app/signup_selecttype.html')


@csrf_exempt
def signup_com(request):
    # user가 로그인 상태시 main으로 리다이렉트
    if request.user.is_authenticated:
        return redirect('index')

    context = {}
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

        else:
            context['form'] = form

    return render(request, 'app/signup_com.html', context)


@csrf_exempt
def signup_official(request):
    # user가 로그인 상태시 main으로 리다이렉트
    if request.user.is_authenticated:
        return redirect('index')

    context = {}
    if request.method == 'POST':
        form = AgencyRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

        else:
            context['form'] = form

    return render(request, 'app/signup_official.html', context)


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
                return redirect('index')
        else:
            context['form'] = form
    return render(request, 'app/login.html', context)


def logout_accounts(request):
    logout(request)
    return redirect('index')


def service_writework(request):
    return render(request, 'app/service_writework.html')
