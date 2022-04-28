from django.urls import path
from accounts import views, email_auth

app_names = 'accounts'

urlpatterns = [
    path('login/', views.login_accounts, name='login'),
    path('logout/', views.logout_accounts, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('signup_official', views.signup_official, name='signup_official'),
    path('signup_company', views.signup_company, name='signup_company'),
    path('email_auth/<str:uid64>/<str:token>', email_auth.EmailAuthView.get, name='email_auth')
]
