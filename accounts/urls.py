from django.urls import path
from accounts import views, email_auth

app_names = 'accounts'

urlpatterns = [
    path('login/', views.login_accounts, name='login'),
    path('logout/', views.logout_accounts, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('signup_official', views.signup_official, name='signup_official'),
    path('signup_company', views.signup_company, name='signup_company'),
    path('pwchange/', views.pwchange, name='pwchange'),
    path('edit_company/', views.edit_company, name='edit_company'),
    path('edit_official/', views.edit_official, name='edit_official'),
    path('my_business/', views.my_business, name='my_business'),
    path('my_qna/', views.my_qna, name='my_qna'),
    path('email_auth/<str:uid64>/<str:token>', email_auth.EmailAuthView.get, name='email_auth'),
    path('signup_agreement/', views.signup_agreement, name='signup_agreement'),
]