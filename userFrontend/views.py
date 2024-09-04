from venv import logger
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login as auth_login,logout as auth_logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from mainBackend.models import *
from mainBackend.forms import *

# Create your views here.
@login_required
def start(request):
    
    return render(request , 'start.html')

@login_required
def base(request):
    
    return render(request , 'base.html')


def lendingPage(request):
    
    return render(request , 'lendingPage.html')

@login_required()
def PropertyPage(request):
    
    return render(request , 'PropertyPage.html')

@login_required()
def start2(request):
    
    return render(request , 'start2.html')

@login_required()
def userCategory(request):
    
    return render(request , 'userCategory.html')

@login_required()
def basicUsersPage(request):

    properties = Property.objects.filter(verificationStatus=True)
     # Get form inputs
    price = request.POST.get('price')
    category = request.POST.get('category')
    rooms = request.POST.getlist('rooms')

    # Filter by price
    # if price:
    #     properties = properties.filter(PropertyPrice=price)

    # Filter by category
    if category:
        properties = properties.filter(PropertyType=category)

    # Filter by rooms
    # if rooms and 'all' not in rooms:
    #     room_filters = {
    #         'studio': 1,
    #         '2': 2,
    #         '3': 3,
    #         'house': 4,  # assuming 4 represents 
    #     }
    #     room_values = [room_filters[room] for room in rooms if room in room_filters]
    #     properties = properties.filter(number_of_rooms__in=room_values)
    return render(request , 'basicUsersPage.html',{'properties':properties})

@login_required
def basicUsersArea(request):
    properties = Property.objects.filter(verificationStatus=True)
    return render(request, 'basicUsersArea.html', {'properties': properties})

@login_required
def filter_properties(request):
    category = request.GET.get('category')
    price = request.GET.get('price')
    preference = request.GET.get('preference')
    
    if category and price and preference :
        properties = Property.objects.filter(verificationStatus=True, PropertyType=category,PropertyPrice=price)
    elif category and price:
        properties = Property.objects.filter(verificationStatus=True, PropertyType=category,PropertyPrice=price)
    elif category:
         properties = Property.objects.filter(verificationStatus=True, PropertyType=category)
    elif price:
         properties = Property.objects.filter(verificationStatus=True,PropertyPrice=price)
    else:
        properties = Property.objects.filter(verificationStatus=True)
    
    properties_data = list(properties.values())
    return JsonResponse({'properties': properties_data})


@login_required
def ownerUsersPage(request):
    
    return render(request , 'ownerUsersPage.html')

@login_required
def ownerAllProperties(request):
    
    return render(request , 'ownerAllProperties.html')

@login_required
def ownerNotifications(request):
    
    return render(request , 'ownerNotifications.html')

@login_required
def ownerProperties(request):
    userId = request.user.UserId
    print(userId)
    Properties = Property.objects.filter(OwnerId = userId)
    return render(request , 'ownerProperties.html',{'Properties': Properties})

@login_required
def ownerManagementCenter(request):
    
    return render(request , 'ownerManagementCenter.html')

# @login_required
def addProperty(request):
    if request.method == "POST":
        # print(request.POST)
        user = request.user
        propertyType = request.POST['PropertyType']
        propertyTypeF = ''.join(propertyType)
        form = PropertyForm(request.POST, request.FILES)
        files = request.GET.getlist('PropertyOwningFiles')
         #cette ligne ne marche pas 
        form.PropertyOwningFiles = files
        form.PropertyType = propertyTypeF
        print(propertyTypeF)
        if form.is_valid():
            form = PropertyForm(request.POST, request.FILES)
            form.save()
            PropertyInstance = Property.objects.order_by('-id').first()
            PropertyInstance.OwnerId = user
            PropertyInstance.save()
            # Création de l'objet PropertyNotification
            notification = PropertyNotification(PropertyId=PropertyInstance)
            notification.save()
            return redirect('addProperty')  
        else:
            logger.error('Form errors: %s', form.errors)
            # return HttpResponse('ca ne marche pas')
    else:
        form = PropertyForm()
        
        
    return render(request , 'addProperty.html',{'form': form})

@login_required
def modifyPropertyPage(request):
    # property_instance = get_object_or_404(Property, id=property_id)
    properties = Property.objects.all()

    return render(request,'modifyPropertyPage.html',{'properties':properties})

@login_required
def modifyProperty(request,property_id):
    property_instance = get_object_or_404(Property, id=property_id)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property_instance)
        if form.is_valid():
            form.save()  
            return redirect('modifyPropertyPage')  

    else:
        form = PropertyForm(instance=property_instance)
    return render(request, 'modifyProperty.html', {'form': form})

@login_required
def deleteProperty(request, property_id):
    property_instance = get_object_or_404(Property, id=property_id)
    property_instance.delete()
          
    return redirect('modifyPropertyPage')

@login_required
def verifyStatutOwner(request):
    
    return render(request , 'verifyStatutOwner.html')

@login_required
def verifyStatutClient(request):
    
    return render(request , 'verifyStatutClient.html')

@login_required()
def properties(request):
    
    return render(request , 'properties.html')

@login_required
def propertyViewMore(request):
    
    return render(request , 'propertyViewMore.html')


@login_required
def notifications(request):
    
    return render(request , 'notifications.html')

@login_required
def charts(request):
    
    return render(request , 'charts.html')



def clientPage(request):
    properties = Property.objects.all()[:3]
    return render(request , 'clientPage.html', {'properties': properties})
    # return render(request , 'clientPage.html')

def contact(request):
    
    return render(request , 'contact.html')


def listing(request):
    properties = Property.objects.filter(verificationStatus=True)    
    return render(request , 'listing.html', {'properties': properties})

# Algorithme de filtrage 

def filter(request):
    pass


# Authentification Views

def register(request):
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
                user.groups.add(Group.objects.get(name='owner'))
                # rediriger vers la page de login
                return redirect('login')
        else:
            logger.error('Form errors: %s', form.errors)
    else:
        form = RegistrationForm()
           
    return render(request, 'register.html',{'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        email = request.POST.get('email')
        if form.is_valid():
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                # connecter l'utilisateur
                auth_login(request, user)
                # condition pour verifier le status de l'utilisateur
                if user.groups.filter(name='admin').exists():
                    return redirect('base')
                elif user.groups.filter(name='owner').exists():
                    return redirect('ownerManagementCenter')
                elif user.groups.filter(name='buyer').exists():
                    return redirect('PropertyPage')
                  # Redirige vers une page après connexion réussie
            else:
                form.add_error(None, 'Invalid email or password')
        else:
            logger.error('Form errors: %s', form.errors)
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def Logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')  # Redirect to the home page or any other page

