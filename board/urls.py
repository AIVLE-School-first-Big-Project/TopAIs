from django.urls import path
from board import views

app_names = 'board'

urlpatterns = [
    path('service/', views.service, name='service'),
    path('coolRoof/', views.service_coolRoof, name='coolRoof'),
    path('roadLine/', views.service_roadLine, name='roadLine'),
    path('write/', views.service_write, name='write'),
]
