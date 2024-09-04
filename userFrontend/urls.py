from django.urls import path
from django.contrib.auth.views import LogoutView

from GestionImmo import settings
from .import views

urlpatterns = [
    path('start/', views.start , name = "start"),
    path('base/', views.base , name = "base"),
    path('clientPage/', views.clientPage , name = "clientPage"),
    path('listing/', views.listing , name = "listing"),
    path('contact/', views.contact , name = "contact"),
    path('lendingPage/', views.lendingPage , name = "lendingPage"),
    path('PropertyPage/', views.PropertyPage , name = "PropertyPage"),
    path('start2/', views.start2 , name = "start2"),
    path('userCategory/', views.userCategory , name = "userCategory"),
    path('register/', views.register , name = "register"),
    path('login/', views.login , name = "login"),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('basicUsersPage/', views.basicUsersPage , name = "basicUsersPage"),
    path('basicUsersArea/', views.basicUsersArea , name = "basicUsersArea"),
    path('filter-properties/', views.filter_properties, name='filter_properties'),
    path('ownerUsersPage/', views.ownerUsersPage , name = "ownerUsersPage"),
    path('ownerAllProperties/', views.ownerAllProperties , name = "ownerAllProperties"),
    path('ownerNotifications/', views.ownerNotifications , name = "ownerNotifications"),
    path('ownerProperties/', views.ownerProperties , name = "ownerProperties"),
    # management center and properties management
    path('ownerManagementCenter/', views.ownerManagementCenter , name = "ownerManagementCenter"),
    path('addProperty/', views.addProperty , name = "addProperty"),
    path('deleteProperty/<int:property_id>', views.deleteProperty , name = "deleteProperty"),
    path('modifyProperty/<int:property_id>', views.modifyProperty , name = "modifyProperty"),
    path('modifyPropertyPage/', views.modifyPropertyPage , name = "modifyPropertyPage"),
    # statues verification
    path('verifyStatutOwner/', views.verifyStatutOwner, name = "verifyStatutOwner"),
    path('verifyStatutClient/', views.verifyStatutClient, name = "verifyStatutClient"),

    path('properties/', views.properties, name = "properties"),
    path('propertyViewMore/', views.propertyViewMore, name = "propertyViewMore"),
    
]