from django.contrib import admin
from django.urls import path
from app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('main/', views.index, name='index'),
    path('albums/', views.albums, name='albums'),
    path('blog/', views.blog, name='blog'),
    path('service_coolroof/', views.service_coolroof, name='service_coolroof'),
    path('service_roadline/', views.service_roadline, name='service_roadline'),
    path('elements/', views.elements, name='elements'),
    path('event/', views.event, name='event'),
    path('login/', views.login_accounts, name='login'),
    path('logout', views.logout_accounts, name='logout'),
    path('signup_com/', views.signup_com, name='signup_com'),
    path('signup_selecttype/', views.signup_selecttype, name='signup_selecttype'),
    path('signup_official/', views.signup_official, name='signup_official'),
    path('service_writework/', views.service_writework, name='service_writework'),
]
