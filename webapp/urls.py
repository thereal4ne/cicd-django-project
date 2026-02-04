from django.urls import path
from .views import task_list

urlpatterns = [
    # Change 'tasks/' to '' to make it the homepage
    path('', task_list, name='task_list'),
]