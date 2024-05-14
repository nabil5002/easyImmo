from django.shortcuts import render
from mainBackend.models import *

# Create your views here.

def index(request):
    
    return render(request , 'index.html')

def users(request):
    
    return render(request , 'users.html')

def properties(request):
    
    return render(request , 'properties.html')

def operations(request):
    
    return render(request , 'operations.html')

def officers(request):
    
    return render(request , 'officers.html')
def notifications(request):
    
    return render(request , 'notifications.html')


def charts(request):
    
    return render(request , 'charts.html')



