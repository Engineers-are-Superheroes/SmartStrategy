from django.shortcuts import render, redirect

#create home view 
def home_view(request):
    return render(request, 'home.html')

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