from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .forms import BoardWriteForm, CommentWriteForm
from .models import Board, Comment


def service(request):
    return render(request, 'service.html')


def service_coolRoof(request):
    return render(request, 'service_coolRoof.html')


def service_roadLine(request):
    return render(request, 'service_roadLine.html')


@login_required(login_url='/accounts/login')
def service_write(request):
    context = {}

    if request.method == 'POST':
        form = BoardWriteForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user_id = request.session['_auth_user_id']
            form.save()
            return redirect('board_list')
        else:
            context['form'] = form
    return render(request, 'service_write.html', context)


@login_required(login_url='/accounts/login')
def listing(request):
    return render(request, 'board_list.html')
