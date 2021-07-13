from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from django.forms.widgets import PasswordInput


class CustomLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(widget=PasswordInput)
    password2 = forms.CharField(widget=PasswordInput)
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]