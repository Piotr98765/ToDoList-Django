from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Task
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect



def index(request):
    todo_items=Task.objects.all().order_by("-created")
    return render(request, 'base/index.html', { "todo_items": todo_items})

@csrf_exempt
def add_task(request):
    
    created = timezone.now()
    content=request.POST["content"]
    created_task=Task.objects.create(created=created, title=content)
   
    return HttpResponseRedirect("/")

@csrf_exempt
def delete_task(request, todo_item_id):
    task = Task.objects.get(id=todo_item_id)
    task.delete()
    return HttpResponseRedirect("/")

@csrf_exempt
def clear(request):
    todo_items=Task.objects.all()
    todo_items.delete()
    return HttpResponseRedirect("/")

    