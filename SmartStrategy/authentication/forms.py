#create django login form
from django import forms

form_attr = {"class" : "input-input input"}

class VolunteerRegisterForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs=form_attr))
    full_name = forms.CharField(widget=forms.TextInput(attrs=form_attr))
    password = forms.CharField(widget=forms.PasswordInput(attrs=form_attr))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=form_attr))
    country = forms.CharField(widget=forms.TextInput(attrs=form_attr))
    city = forms.CharField(widget=forms.TextInput(attrs=form_attr))
    phone_number = forms.CharField( widget=forms.TextInput(attrs=form_attr))
    skills = forms.CharField( widget=forms.TextInput(attrs=form_attr))

class VolunteerLoginForm(forms.Form):
    email = forms.EmailField( widget=forms.EmailInput(attrs=form_attr))
    password = forms.CharField(widget=forms.PasswordInput(attrs=form_attr))