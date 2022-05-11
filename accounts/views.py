from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test

from .forms import AuthenticationForm, AgencyRegistrationForm, CompanyRegistrationForm
from .email_auth import EmailAuthView
from .models import Agency, Company

from board.models import Board, Comment
from board.models import Question

login_url = '/accounts/login'


def is_writable(user):
    return user.is_staff or is_Agency(user)


def is_company(user):
    return user.user_type == 'Company'


def is_Agency(user):
    return user.user_type == 'Agency'


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


@csrf_exempt
@login_required(login_url=login_url)
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


@csrf_exempt
@login_required(login_url=login_url)
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


@login_required(login_url=login_url)
def logout_accounts(request):
    logout(request)
    return redirect('index')


@csrf_exempt
@login_required(login_url=login_url)
@user_passes_test(is_company)
def edit_company(request):
    info = Company.objects.get(pk=request.user)
    context = {
        'info': info
    }

    if request.method == 'POST':
        info.comp_name = request.POST.get('compName', '')
        info.comp_homepage = request.POST.get('compHompage', '')
        info.comp_category = request.POST.get('compCategory', '')
        info.username = request.POST.get('userName', '')
        info.phone = request.POST.get('userPhone', '')

        info.save()

    return render(request, 'edit_company.html', context)


@csrf_exempt
@login_required(login_url=login_url)
@user_passes_test(is_Agency)
def edit_official(request):
    info = Agency.objects.get(pk=request.user)

    context = {
        'info': info,
    }

    if request.method == 'POST':
        info.area = request.POST.get('area', '')
        info.username = request.POST.get('username', '')
        info.phone = request.POST.get('phone', '')

        info.save()
        return redirect('edit_official')

    return render(request, 'edit_official.html', context)


@csrf_exempt
@login_required(login_url=login_url)
def my_business(request):
    # 지자체
    if is_Agency:
        board = Board.objects.filter(user_id=request.user)

    # 시공업체
    elif is_company:
        comment_list = Comment.objects.filter(user_id=request.user).values('board')
        board = Board.objects.filter(pk__in=comment_list)

    # 관리자
    else:
        board = Board.objects.order_by('-id')

    list_per = 10
    page_per = 5

    paginator = Paginator(board, list_per)

    page_number = request.GET.get('page', 1)
    board_list = paginator.get_page(page_number)

    start_page = (int(page_number) - 1) // page_per * page_per + 1
    end_page = start_page + page_per - 1

    if end_page > paginator.num_pages:
        end_page = paginator.num_pages

    context = {
        'board_list': board_list,
        'start_page': start_page,
        'end_page': end_page,
    }
    return render(request, 'my_business.html', context)


@csrf_exempt
@login_required(login_url=login_url)
def my_qna(request):
    if request.user.is_staff:
        question = Question.objects.order_by('-id')
    else:
        question = Question.objects.filter(user_id=request.user.id).order_by('-id')
    list_per = 10
    page_per = 5

    paginator = Paginator(question, list_per)

    page_number = request.GET.get('page', 1)
    question_list = paginator.get_page(page_number)

    start_page = (int(page_number) - 1) // page_per * page_per + 1
    end_page = start_page + page_per - 1

    if end_page > paginator.num_pages:
        end_page = paginator.num_pages

    context = {
        'question_list': question_list,
        'start_page': start_page,
        'end_page': end_page,
    }
    return render(request, 'my_qna.html', context)


def signup_agreement(request):
    if request.user.is_authenticated:
        return redirect('index')

    return render(request, 'signup_agreement.html')
