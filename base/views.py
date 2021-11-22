from django.shortcuts import render, redirect
from .models import Task
from django.http import HttpResponse



def index(request):
    
    return render(request, 'base/index.html')

    