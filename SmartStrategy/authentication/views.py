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
        user = User.objects.create_user(
            username=form.data['email'],
            email=form.data['email'],
            password=form.data['password'],
            first_name=form.data['full_name'],
        )
        Volunteer.objects.create(
            user=user,
            country=form.data['country'],
            city=form.data['country'],
            phone_number=form.data['country'],
        )
        login(request, user)
        return redirect('strategy:home')
    return render(request, 'authentication/register.html', context)
