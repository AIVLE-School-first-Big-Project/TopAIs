from django.urls import path
from board import views

app_names = 'board'

urlpatterns = [
    path('service/', views.service, name='service'),
    path('coolRoof/', views.service_coolRoof, name='coolRoof'),
    path('roadLine/', views.service_roadLine, name='roadLine'),
    path('qna_write/', views.qna_write, name='qna_write'),
    path('qna_list/', views.qna_list, name='qna_list'),
    path('write/', views.service_write, name='write'),
    path('list/', views.listing, name='board_list'),
    path('detail/<int:pk>', views.board_detail_view, name='board_detail'),
]
