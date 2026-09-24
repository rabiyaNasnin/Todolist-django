from django.urls import path
from . import api_views

urlpatterns = [
    path('tasks/',api_views.task_list,name='task-list'),
    path('tasks/<int:pk>/',api_views.task_detail,name='task-detail'),
]