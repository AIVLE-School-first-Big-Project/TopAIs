from django.shortcuts import render

def index(request):
    return render(request, 'app/index.html') 

def service(request):
    return render(request, 'app/service.html')

def board(request):
    return render(request, 'app/board.html') 

def qna(request):
    return render(request, 'app/qna.html')

def login(request):
    return render(request, 'app/login.html')