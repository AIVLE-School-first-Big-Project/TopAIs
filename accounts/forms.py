from django.contrib.auth.hashers import check_password
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, get_user_model
from .models import Agency, Company, User

USER_INFO = ['username', 'user_id', 'password1', 'email', 'phone', ]
USER_UPDATE = ['userId', 'userName', 'userEmail', 'userPhone']


class RegistrationForm(UserCreationForm, forms.ModelForm):
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            _ = User.objects.get(email=email)
        except User.DoesNotExist as e:
            return email
        raise forms.ValidationError(f"Email {email} is already in use.")

    def clean_user_id(self):
        user_id = self.cleaned_data['user_id']
        try:
            _ = User.objects.get(user_id=user_id)
        except User.DoesNotExist as e:
            return user_id
        raise forms.ValidationError(f"User_id {user_id} is already in use.")

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        try:
            _ = User.objects.get(phone=phone)
        except User.DoesNotExist as e:
            return phone
        raise forms.ValidationError(f"Phone {phone} is already in use.")


class CompanyRegistrationForm(RegistrationForm):
    class Meta:
        model = Company
        fields = (
            *USER_INFO,
            'comp_category', 'comp_name', 'comp_homepage',
        )


class AgencyRegistrationForm(RegistrationForm):
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


class AuthenticationForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('user_id', 'password')

    def clean(self):
        if self.is_valid():
            user_id = self.cleaned_data['user_id']
            password = self.cleaned_data['password']
            if not authenticate(user_id=user_id, password=password):
                raise forms.ValidationError("Invalid login")

# class UserUpdateForm(UserChangeForm, forms.ModelForm):
#     def clean_phone(self):
#         phone = self.cleaned_data['phone']
#         try:
#             _ = User.objects.get(phone=phone)
#         except User.DoesNotExist as e:
#             return phone
#         raise forms.ValidationError(f"Phone {phone} is already in use.")

# class CompanyUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Company
#         fields = (
#             *USER_UPDATE,
#             'compName', 'compHompage', 'compCategory',
#         )
