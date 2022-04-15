from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('main/', views.index,name='index'),
    path('albums/', views.albums,name='albums'),
    path('blog/', views.blog,name='blog'),
    path('contact/', views.contact,name='contact'),
    path('elements/', views.elements,name='elements'),
    path('event/', views.event,name='event'),
    path('login/', views.login,name='login'),
]