from django.shortcuts import render
from mainBackend.models import *

# Create your views here.

def start(request):
    
    return render(request , 'start.html')

def register(request):
    
    return render(request , 'register.html')

def login(request):
    
    return render(request , 'login.html')

def verifyStatutOwner(request):
    
    return render(request , 'verifyStatutOwner.html')

def verifyStatutClient(request):
    
    return render(request , 'verifyStatutClient.html')

def notifications(request):
    
    return render(request , 'notifications.html')


def charts(request):
    
    return render(request , 'charts.html')

