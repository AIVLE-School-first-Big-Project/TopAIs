from django.shortcuts import render

def albums(request):
    return render(request, 'app/albums.html') 

def blog(request):
    return render(request, 'app/blog.html') 

def contact(request):
    return render(request, 'app/contact.html') 

def elements(request):
    return render(request, 'app/elements.html') 

def event(request):
    return render(request, 'app/event.html') 

def index(request):
    return render(request, 'app/index.html') 

def login(request):
    return render(request, 'app/login.html')