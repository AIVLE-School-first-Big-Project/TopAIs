from django.contrib import admin
from django.urls import path
from app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('albums/', views.albums,name=' albums'),
    path('blog/', views.blog, name='blog'),
    path('elements/', views.elements, name='elements'),
    path('event/', views.event, name='event'),
    path('login/', views.login, name='login'),
]
