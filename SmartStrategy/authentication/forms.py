#create django login form
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Volunteer, Organization

class VolunteerRegisterForm(UserCreationForm):
    email = forms.EmailField()
        
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class VolunteerLoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)