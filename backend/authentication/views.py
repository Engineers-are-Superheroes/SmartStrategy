from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from .models import Volunteer_User
# Create your views here.

class Volunteer_Login(View):

    def get(self, request):
        context = {

        }
        return render(request, 'volunteer_login.html', context)

    def post(self, request):
        data = request.data
        #get user with username and password
        user = authenticate(username=data['username'], password=data['password'])

