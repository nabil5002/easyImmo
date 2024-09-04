from venv import logger
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from mainBackend.forms import RegistrationForm
from mainBackend.models import *
from django.contrib.auth.models import Group


# Create your views here.
@login_required
def index(request):
    
    return render(request , 'index.html')

@login_required
def users(request):
    
    return render(request , 'users.html')

@login_required
def properties(request):
    
    return render(request , 'properties.html')

@login_required
def operations(request):
    
    return render(request , 'operations.html')

@login_required
def officers(request):
    
    return render(request , 'officers.html')

@login_required
def notifications(request):
    
    return render(request , 'notifications.html')

@login_required
def propertiesNotification(request):
    notifications = PropertyNotification.objects.all()
    return render(request , 'propertiesNotification.html',{'notifications':notifications})

@login_required
def statusVerification(request,id):
    notification = get_object_or_404(PropertyNotification,id=id)
    propertyId = notification.PropertyId.id
    property = get_object_or_404(Property,id=propertyId)
    property.verificationStatus = True
    property.save()
    if property.verificationStatus == True:
        notification.delete()
    #     pass
    return redirect('propertiesNotification')
    
@login_required
def usersNotification(request):
    
    return render(request , 'usersNotification.html')

@login_required
def charts(request):
    
    return render(request , 'charts.html')

@login_required
def createAccount(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Vérifiez que le nom d'utilisateur n'est pas déjà pris
            if User.objects.filter(email=form.cleaned_data.get('email')).exists():
                return render(request, 'register.html', {'error': 'Username is already taken'})
            else:
                #recuperer le status du compte 
                status = form.cleaned_data['UserStatus']
                # Créez un nouvel utilisateur
                user = form.save()
                #condition pour assigner un groupe a l'utilisateur
                if status == "Admin":
                    user.groups.add(Group.objects.get(name='admin'))
                elif status == "Owner":
                    user.groups.add(Group.objects.get(name='owner'))
                elif status == "Buyer":
                    user.groups.add(Group.objects.get(name='buyer'))
                # rediriger vers la page de login
                # return redirect('login')
        else:
            logger.error('Form errors: %s', form.errors)
    else:
        form = RegistrationForm()
           
    return render(request, 'createAccount.html',{'form': form})
    



