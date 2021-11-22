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
def delete_task(request, task_id):
    Task.objects.get(id=task_id).delete()
    return HttpResponseRedirect("/")

    