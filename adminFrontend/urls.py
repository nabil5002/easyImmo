from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name = "index"),
    path('users/', views.users , name = "users"),
    path('properties/', views.properties , name = "properties"),
    path('operations/', views.operations, name = "operations"),
    path('officers/', views.officers, name = "officers"),
    path('notifications/', views.notifications, name = "notifications"),
    path('charts/', views.charts, name = "charts"),
    # path('supprimerProduit/', views.supprimerProduit, name = "supprimerProduit"),
    # path('vente/', views.vente, name = "vente"),
    # path('client/', views.client, name = "client"),
    # path('voirCategorie/', views.voirCategorie, name = "voirCategorie"),
    # path('recuDeVente/', views.recuDeVente, name = "recuDeVente"),
    # path('updateProduit/<int:pk>', views.updateProduit, name = "updateProduit"),
    # path('choixPayement/', views.choixPayement, name = "choixPayement"),
]