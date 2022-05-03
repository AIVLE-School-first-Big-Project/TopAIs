from django.urls import path
from map import views

app_names = 'map'

urlpatterns = [
    path('coolRoof/', views.service_coolRoof),
    path('roadLine/', views.service_roadLine),
]
