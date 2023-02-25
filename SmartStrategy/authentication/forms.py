#create django login form
from django import forms

class VolunteerRegisterForm(forms.Form):
    email = forms.EmailField()
    full_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    country = forms.CharField()
    city = forms.CharField()
    phone_number = forms.CharField()
    skills = forms.CharField()

class VolunteerLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)