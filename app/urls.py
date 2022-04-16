from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('main/', views.index,name='index'),
    path('board/', views.board,name='board'),
    path('qna/', views.qna,name='qna'),
    path('service/', views.service,name='service'),
    path('login/', views.login,name='login'),
]