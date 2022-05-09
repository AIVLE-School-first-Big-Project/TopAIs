from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from board import views

app_names = 'board'

urlpatterns = [
    path('service/', views.service, name='service'),
    path('coolRoof/', views.service_coolRoof, name='coolRoof'),
    path('roadLine/', views.service_roadLine, name='roadLine'),
    path('qna/', views.qna, name='qna'),
    path('qna/detail/<int:pk>', views.qna_detail_view, name='qna_detail'),
    # path('qna/delete/<int:pk>', views.qna_write, name='qna_write'),
    # path('qna/edit/<int:pk>', views.qna_write, name='qna_write'),
    path('qna/write/', views.qna_write, name='qna_write'),
    path('write/', views.service_write, name='write'),
    path('list/', views.listing, name='board_list'),
    path('detail/<int:pk>', views.board_detail_view, name='board_detail'),
    path('edit/<int:pk>', views.board_edit_view, name='board_edit'),
    path('delete/<int:pk>', views.board_delete_view, name='board_delete'),
    path('delete/<int:board_pk>/<int:comment_pk>', views.comment_delete_view, name='comment_delete'),
    path('download/<int:pk>/<int:comment_pk>', views.file_download, name='file_download'),
    # path('detail/<int:pk>', views.)
]
urlpatterns += static(settings.STATIC_URL, documnet_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, documnet_root=settings.MEDIA_ROOT)
