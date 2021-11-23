from django.shortcuts import render
from .models import Todo

def todolist(request):
    tasks = Todo.objects.all()
    return render(request, 'todolist/todolist.html', {'tasks': tasks})