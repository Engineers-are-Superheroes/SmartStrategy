from django.shortcuts import render, redirect
import requests

#create home view 
def home_view(request):

    return render(request, 'home.html')

def job_list_view(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('authentication:register')
    #fetch data from red cross API
    url = 'https://goadmin.ifrc.org/api/v2/event/?is_featured=1'
    response = requests.get(url)
    response = response.json()
    events = response['results']

    context = {
        'events': events,
    } 
    return render(request, 'jobs/jobs.html', context)

    

def job_task_view(request):
    user = request.user
    #generate job details based on keywords