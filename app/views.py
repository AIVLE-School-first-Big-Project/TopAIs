from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from app.email_auth import EmailAuthView
from app.forms import CompanyForm, AgencyForm


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


def login(request):
    return render(request, 'app/login.html')


def signup_selecttype(request):
    return render(request, 'app/signup_selecttype.html')


@csrf_exempt
def signup_com(request):
    # user가 로그인 상태시 main으로 리다이렉트
    if request.user.is_authenticated:
        return redirect('index')

    context = {}
    if request.method == 'POST':
        form = CompanyForm(request.POST)

        if form.is_valid():
            form.save()
            EmailAuthView.post(request, form.data)
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
        form = AgencyForm(request.POST)

        if form.is_valid():
            form.save()
            EmailAuthView.post(request, form.data)
            return redirect('login')

        else:
            context['form'] = form

    return render(request, 'app/signup_official.html', context)


def service_writework(request):
    return render(request, 'app/service_writework.html')
