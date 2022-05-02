from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .forms import BoardWriteForm, CommentWriteForm
from .models import Board, Comment


def service(request):
    return render(request, 'service.html')


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
    board_list = Board.objects.order_by('-id')
    paginator = Paginator(board_list, 10)

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    start_page = (int(page_number) - 1) // 10 * 10 + 1
    end_page = start_page + 9

    if end_page > paginator.num_pages:
        end_page = paginator.num_pages

    context = {
        'page_info': page_obj,
        'page_range': range(start_page, end_page + 1)
    }

    print(board_list)
    print(start_page, end_page)
    return render(request, 'board_list.html')
