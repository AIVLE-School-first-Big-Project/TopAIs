from django import forms
from accounts.models import User, Company, Agency
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

