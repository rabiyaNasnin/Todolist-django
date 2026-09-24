from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [

    path(
        'login/',
         LoginView.as_view(template_name='login.html'),
         name='login'
    ),
    path(
        'logout/',
        LogoutView.as_view(),
        name='logout'
    ),
    path(
        '', views.index, name='index'
    ),
    path(
        'update/<int:pk>/',
         views.updateTask,
         name='update_task'
    ),
    path(
        'delete/<int:pk>/',
        views.deleteTask, 
        name='delete_task'
    ),
         
]
