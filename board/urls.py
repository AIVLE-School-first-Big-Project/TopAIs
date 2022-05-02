from django.urls import path
from board import views

app_names = 'board'

urlpatterns = [
    path('service/', views.service, name='service'),
    path('write/', views.service_write, name='write'),
    path('list/', views.listing, name='board_list'),
]
