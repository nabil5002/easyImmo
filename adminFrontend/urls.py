from django.urls import path
from .import views

urlpatterns = [
    path('', views.index , name = "index"),
    path('users/', views.users , name = "users"),
    path('properties/', views.properties , name = "properties"),
    path('operations/', views.operations, name = "operations"),
    path('officers/', views.officers, name = "officers"),
    path('notifications/', views.notifications, name = "notifications"),
    path('propertiesNotification/', views.propertiesNotification, name = "propertiesNotification"),
    path('statusVerification/<int:id>', views.statusVerification, name='statusVerification'),
    path('usersNotification/', views.usersNotification, name = "usersNotification"),
    path('charts/', views.charts, name = "charts"),
    path('createAccount/', views.createAccount, name = "createAccount"),
    
]