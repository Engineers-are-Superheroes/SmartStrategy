from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Volunteer
from .forms import VolunteerRegisterForm, VolunteerLoginForm
# Create your views here.

def login_view(request):
    context = {
        'form': VolunteerLoginForm()
    }
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('strategy:home')
        else:
            context['error'] = 'Username or password is incorrect'
    return render(request, 'authentication/login.html', context)       

def logout_view(request):
    logout(request)
    return redirect('strategy:home')

def register_view(request):
    context = {
        'form': VolunteerRegisterForm()
    }
    if request.method == 'POST':
       #register user
        form = VolunteerRegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['full_name'],
            )
            Volunteer.objects.create(
                user=user,
                country=form.cleaned_data['country'],
                city=form.cleaned_data['city'],
                phone_number=form.cleaned_data['phone_number'],
            )
            login(request, user)
            return redirect('strategy:home')
        else:
            context['error'] = 'form filled out incorrectly'
    return render(request, 'authentication/register.html', context)
