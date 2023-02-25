from django.shortcuts import render

#create home view 
def home_view(request):
    return render(request, 'home.html')
