from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model

from .forms import AuthenticationForm, AgencyRegistrationForm, CompanyRegistrationForm
from .email_auth import EmailAuthView
from .models import Agency, Company

from board.models import Board, Comment
from map.models import Building


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
                if not user.email_auth:
                    messages.info(request, '　　　　　이메일 인증 후 로그인해주세요.')
                    return redirect('login')
                else:
                    login(request, user)
                    next_url = request.GET.get('next')
                    if next_url:
                        return redirect(next_url)
                    return redirect('index')
        else:
            context['form'] = form
    return render(request, 'login.html', context)


def pwchange(request):
    if request.method == 'POST':
        user_id = request.session.get('_auth_user_id')
        user_pw = request.POST.get('password1')
        user_pw_check = request.POST.get('password2')

        if user_pw_check != user_pw:
            messages.info(request, '비밀번호가 일치하지 않습니다.')
            return HttpResponseRedirect(reverse('pwchange'))
        else:
            user = get_user_model().objects.get(id=user_id)
            user.set_password(user_pw)
            user.save()
            messages.info(request, '　　　　　　비밀번호가 변경되었습니다. 　　　　　　　다시 로그인 해주세요.')
            update_session_auth_hash(request, request.user)
            return HttpResponseRedirect(reverse('login'))
    return render(request, 'pwchange.html')


def withdraw(request):
    if request.method == 'POST':
        user = request.user
        password = request.POST.get('password1', '')
        confirm_password = request.POST.get('password2', '')

        if password != confirm_password:
            return HttpResponseRedirect(reverse('delete'))

        if check_password(password, user.password):
            user.delete()
            logout(request)
            return redirect('index')

        else:
            return HttpResponseRedirect(reverse('delete'))

    return render(request, 'delete.html')


def logout_accounts(request):
    logout(request)
    return redirect('index')


def edit_company(request):
    info = Company.objects.get(pk=request.user)

    context = {
        'info': info
    }
    return render(request, 'edit_company.html', context)


def edit_official(request):
    info = Agency.objects.get(pk=request.user)

    # if request.method == 'POST':
    #     form = AgencyUpdateForm(request.POST)
    #     if form.is_valid():
    #         print(form.data)
    # else:
    #     form = AgencyUpdateForm()
    # if request.method == 'POST':
    #     form = AgencyRegistrationForm(request.POST)
    # else:
    #     form = AgencyRegistrationForm(request.POST)
    context = {
        'info': info,
        # 'form': form,
    }
    return render(request, 'edit_official.html', context)


def my_business(request):
    # 지자체
    if get_user_model().is_Agency(request.user):
        board_list = Board.objects.filter(user_id=request.user)

    # 시공업체
    elif get_user_model().is_Company(request.user):
        comment_list = Comment.objects.filter(user_id=request.user)
        board_list = comment_list

    # 관리자
    else:
        board_list = Board.objects.order_by('-id')

    context = {
        'board_list': board_list,
    }
    return render(request, 'my_business.html', context)


def my_qna(request):
    return render(request, 'my_qna.html')


def signup_agreement(request):
    return render(request, 'signup_agreement.html')
