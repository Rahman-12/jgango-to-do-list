from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Task


def index(request):
    tasks= Task.objects.all()
    return render(request,"index.html",{"tasks":tasks})