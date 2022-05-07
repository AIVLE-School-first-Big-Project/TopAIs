from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from board import views

app_names = 'board'

urlpatterns = [
    path('service/', views.service, name='service'),
    path('coolRoof/', views.service_coolRoof, name='coolRoof'),
    path('roadLine/', views.service_roadLine, name='roadLine'),
    path('qna_write/', views.qna_write, name='qna_write'),
    path('faq/', views.faq, name='faq'),
    path('write/', views.service_write, name='write'),
    path('list/', views.listing, name='board_list'),
    path('detail/<int:pk>', views.board_detail_view, name='board_detail'),
    # path('edit/<int:pk>', views.board_edit_view, name='board_edit),
    path('delete/<int:pk>', views.board_delete_view, name='board_delete'),
    path('download/<int:pk>', views.file_download, name='file_download'),
]
urlpatterns += static(settings.STATIC_URL, documnet_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, documnet_root=settings.MEDIA_ROOT)
