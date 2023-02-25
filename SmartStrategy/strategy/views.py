from django.shortcuts import render

#create home view 
def home_view(request):
    return render(request, 'home.html')

def job_list_view(request):
    user = request.user
    

    #fetch data from red cross API
    pass

def job_task_view(request):
    user = request.user
    #generate job details based on keywords