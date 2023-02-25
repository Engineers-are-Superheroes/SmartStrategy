from django.shortcuts import render

#create home view 
def home_view(request):
    return render(request, 'home.html')

def getJobs(request):
    #fetch data from red cross API
    pass

def showJob(request):
    user = request.user
    #generate job details based on keywords