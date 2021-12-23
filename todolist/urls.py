from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('delete_all', views.delete_all, name='delete-all'),
    path('delete/<int:task>/', views.delete, name="delete"),
    path('change_to_done/<int:task>/', views.change_to_done, name="change_to_done"), 


]