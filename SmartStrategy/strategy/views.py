from django.shortcuts import render
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
    

    #fetch data from red cross API
    pass

def job_task_view(request):
    user = request.user
    #generate job details based on keywords