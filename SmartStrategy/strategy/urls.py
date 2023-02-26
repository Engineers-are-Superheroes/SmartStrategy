from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('job_list/', views.job_list_view, name='job_list'),
    path('job_task/(?P<event_name>[0-9]+)/\\Z/', views.job_task_view, name='job_task'),
    path('signedup/<event_name>/<task_name>/', views.signedup_view, name='signedup'),
]