from django import forms
from app.models import User, Company, Agency
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

USER_INFO = ['username', 'user_id', 'password1', 'password2', 'email', 'phone']


class RegistrationForm(UserCreationForm):

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            _ = User.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"Email {email} is already in use.")

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            _ = User.objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"Username {username} is already in use.")


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


# class LoginForm(AuthenticationForm):

