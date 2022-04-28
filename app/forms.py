from django import forms
from app.models import User, Company, Agency
from django.contrib.auth.forms import UserCreationForm

USER_INFO = ['username', 'user_id', 'password1', 'password2', 'email', 'phone']


class RegistrationForm(UserCreationForm):
    # def clean_phone(self):
    #     phone = self.cleaned_data['phone'].lower()
    #     try
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            _ = User.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"Email {email} is already in use.")

    def clean_user_id(self):
        print(self.cleaned_data)
        user_id = self.cleaned_data['user_id']
        try:
            _ = User.objects.get(username=user_id)
        except Exception as e:
            return user_id
        raise forms.ValidationError(f"Username {user_id} is already in use.")


class CompanyForm(RegistrationForm):
    class Meta:
        model = Company
        fields = (
            *USER_INFO,
            'comp_category', 'comp_name', 'comp_homepage',
        )



class AgencyForm(RegistrationForm):
    class Meta:
        model = Agency
        fields = (
            *USER_INFO,
            'area',
        )
    
    # 특정 도메인 사용자 인증
    def clean_email(self):
        email = super().clean_email()
        email_domain = email.split('@')
        if email_domain[-1] != 'naver.com':
            raise forms.ValidationError(f"Email {email} is not official.")
        return email
