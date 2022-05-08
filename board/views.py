import json
import os.path
import urllib.parse
import mimetypes

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404
from django.contrib import messages

from map.models import Building, Business, Facility

from .forms import BoardWriteForm, CommentWriteForm
from .models import Board, Comment, Announcement

login_url = '/accounts/login'


@login_required(login_url=login_url)
@user_passes_test(get_user_model().is_writable)
def service(request):
    return render(request, 'service.html')


@login_required(login_url=login_url)
@user_passes_test(get_user_model().is_writable)
def service_coolRoof(request):
    building = Building.objects.filter(city='부산광역시').values(
        "latitude", "longitude", "city", "county", "district", "number1", "number2")

    areas = {}
    for i in range(len(building)):
        areas[str(i)] = building[i]

    return render(request, 'service_coolRoof.html', context={'areas': areas})


@login_required(login_url=login_url)
@user_passes_test(get_user_model().is_writable)
def service_roadLine(request):
    return render(request, 'service_roadLine.html')


@csrf_exempt
@login_required(login_url=login_url)
@user_passes_test(get_user_model().is_writable)
def service_write(request):
    context = {}

    if request.method == 'POST':
        selected_areas = request.POST.get('selected_area', '')
        if selected_areas:
            context['selected_areas'] = json.loads(selected_areas)
        else:
            selected_areas = request.POST.get('selected_areas', 0)
            if selected_areas:
                context['selected_areas'] = json.loads(selected_areas.replace("'", '"'))
            form = BoardWriteForm(request.POST)
            if form.is_valid():

                form = form.save(commit=False)
                form.user_id = request.session.get('_auth_user_id')
                form.save()

                # 시공대상 건물 저장
                for key, values in context['selected_areas'].items():
                    print(key, type(key))
                    a = Building.objects.filter(id=key)
                    print(a)
                    # Business.objects.create(
                    #     facility_id=Building.objects.get(pk=int(key)),
                    #     board_id=form.id
                    # )

                if request.FILES:
                    for file in request.FILES.getlist('files'):
                        Announcement.objects.create(
                            name=file.name,
                            uploadFile=file,
                            board_id=form.id,
                        )
                return redirect('board_list')
            else:
                context['form'] = form
    return render(request, 'service_write.html', context)


@login_required(login_url=login_url)
def listing(request):
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
    return render(request, 'board_list.html', context)


@login_required(login_url=login_url)
def board_detail_view(request, pk):
    # 댓글 작성
    if request.method == 'POST':
        form = CommentWriteForm(request.POST)
        if form.is_valid():
            print(form.data)

            # 첨부 파일
            if request.FILES:
                for file in request.FILES['files']:
                    print(file)

    board = get_object_or_404(Board, pk=pk)
    file = Announcement.objects.filter(board_id__exact=pk)

    # 게시글 작성자 확인
    board_auth = False

    if board.user == request.user:
        board_auth = True

    context = {
        'board': board,
        'file': file,
        'board_auth': board_auth,
    }

    return render(request, 'board_detail.html', context)


@login_required(login_url=login_url)
def board_delete_view(request, pk):
    board = get_object_or_404(Board, pk=pk)

    if board.user == request.user:
        board.delete()
        messages.success(request, "삭제되었습니다.")
        return redirect('board_list')
    else:
        messages.error(request, "본인 게시글이 아닙니다.")
        return redirect('board_detail', pk)


@login_required(login_url=login_url)
def board_edit_view(request, pk):
    board = get_object_or_404(Board, pk=pk)

    if request.method == 'POST':
        if board.user == request.user:
            form = BoardWriteForm(request.POST, instance=board)
            if form.is_valid():
                board = form.save(commit=False)
                board.save()
                messages.success(request, '수정되었습니다.')
                return redirect('board_detail', pk)

    else:
        if board.user == request.user:
            form = BoardWriteForm(instance=board)
            context = {
                'form': form,
            }
            return render(request, 'service_write.html', context)
        else:
            messages.error(request, '본인 게시글이 아닙니다.')
            return redirect('board_detail', pk)


@login_required(login_url=login_url)
def qna_write(request):
    return render(request, 'qna_write.html')


def faq(request):
    return render(request, 'faq.html')


@login_required(login_url=login_url)
def file_download(request, pk):
    announcement = get_object_or_404(Announcement, file_ptr_id=pk)
    url = announcement.uploadFile.url[1:]
    file_url = urllib.parse.unquote(url)

    if os.path.exists(file_url):
        with open(file_url, 'rb') as f:
            quote_file_url = urllib.parse.quote(announcement.name.encode('utf-8'))
            response = HttpResponse(f.read(), content_type=mimetypes.guess_type(file_url)[0])
            response['Content-Disposition'] = 'attachment;filename*=UTF-8\'\'%s' % quote_file_url
            return response
    raise Http404
