from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Todo


def todolist(request):
    tasks = Todo.objects.all()
    return render(request, 'todolist/todolist.html', {'tasks': tasks})

def delete_all(request):
    tasks = Todo.objects.all()
    tasks.delete()
    return redirect('/')

