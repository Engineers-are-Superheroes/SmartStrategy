from django.shortcuts import render, redirect
import requests

#create home view 
def home_view(request):
    # make api call to red cross
    # get jobs
    url = 'https://goadmin.ifrc.org/api/v2/event/?is_featured=1'
    response = requests.get(url)
    response = response.json()
    events = response['results']
    # names = events['name']
    # countries = events['countries']
    # num_affected = events['num_affected']
    # start_date = events['disaster_start_date']
    # ids = events['id']

    return render(request, 'home.html', {'events': events})

def job_list_view(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('authentication:signup')
    #fetch data from red cross API
    job_data = {}

    context = {
        'job_data': job_data
    } 
    return render(request, 'job_list.html', context)

    

def job_task_view(request):
    user = request.user
    #generate job details based on keywords