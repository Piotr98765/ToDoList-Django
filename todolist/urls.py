from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('delete_all', views.delete_all, name='delete-all'),

]