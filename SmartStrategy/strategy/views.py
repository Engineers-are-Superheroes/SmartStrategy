from django.shortcuts import render, redirect
from .processing_jobs.backend import backend
import requests

#create home view 
def home_view(request):

    return render(request, 'home.html')

def info_view(request):
    return render(request, 'jobs/info.html')

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



def job_task_view(request, event_name):
    user = request.user
    if not user.is_authenticated:
        return redirect('authentication:register')
    #generate job details based on keywords
    tasks = [
        {'title': task[0], 'description': task[1]} for task in backend(3691, event_name) if len(task) > 1
    ]
    context = {
        'event_name': event_name,
        'tasks': tasks,
    }

    return render(request, 'jobs/tasks.html', context)


def signedup_view(request, event_name, task_name):
    user = request.user
    if not user.is_authenticated:
        return redirect('authentication:register')
    context = {
        'event_name': event_name,
        'task_name': task_name,
    }
    return render(request, 'jobs/signedup.html', context)