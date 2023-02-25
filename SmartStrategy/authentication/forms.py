#create django login form
from django import forms

form_attr = {"class" : "input-input input"}

class VolunteerRegisterForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class" : "input-input input", "placeholder" : "Email"}))
    full_name = forms.CharField(widget=forms.TextInput(attrs={"class" : "input-input input", "placeholder" : "Full Name"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class" : "input-input input", "placeholder" : "Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=form_attr))
    country = forms.CharField(widget=forms.TextInput(attrs={"class" : "input-input input", "placeholder" : "Country"}))
    city = forms.CharField(widget=forms.TextInput(attrs=form_attr))
    phone_number = forms.CharField( widget=forms.TextInput(attrs={"class" : "input-input input", "placeholder" : "Phone Number"}))
    skills = forms.CharField( widget=forms.TextInput(attrs={ "class" : "input-input input", "placeholder" : "Skills"}))

class VolunteerLoginForm(forms.Form):
    email = forms.EmailField( widget=forms.EmailInput(attrs=form_attr))
    password = forms.CharField(widget=forms.PasswordInput(attrs=form_attr))