from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .forms import BoardWriteForm, CommentWriteForm
from .models import Board, Comment

login_url = '/accounts/login'


def service(request):
    return render(request, 'service.html')


def service_coolRoof(request):
    return render(request, 'service_coolRoof.html')


def service_roadLine(request):
    return render(request, 'service_roadLine.html')


@login_required(login_url=login_url)
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


@login_required(login_url=login_url)
def listing(request):
    board = Board.objects.order_by('-id')
    paginator = Paginator(board, 10)

    page_number = request.GET.get('page', 1)
    board_list = paginator.get_page(page_number)

    start_page = (int(page_number) - 1) // 10 * 10 + 1
    end_page = start_page + 9

    if end_page > paginator.num_pages:
        end_page = paginator.num_pages

    context = {
        'board_list': board_list,
        'page_range': range(start_page, end_page + 1)
    }
    return render(request, 'board_list.html', context)


@login_required(login_url=login_url)
def board_detail_view(request, pk):
    board = get_object_or_404(Board, pk=pk)
    context = {'board': board}
    return render(request, 'board_detail.html', context)
