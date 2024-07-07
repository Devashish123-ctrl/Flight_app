from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields =['email']

class Authentication(AuthenticationForm):
    class Meta:
        model= User
        fields =["email"]