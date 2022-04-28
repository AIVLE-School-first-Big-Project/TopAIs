from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BoardWriteForm, CommentWriteForm


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
            form.uid = request.user
            form.save()
            return redirect('service_write')
        else:
            context['form'] = form
    return render(request, 'service_write.html', context)
