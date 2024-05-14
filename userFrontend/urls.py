from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.start , name = "start"),
    path('register/', views.register , name = "register"),
    path('login/', views.login , name = "login"),
    path('verifyStatutOwner/', views.verifyStatutOwner, name = "verifyStatutOwner"),
    path('verifyStatutClient/', views.verifyStatutClient, name = "verifyStatutClient"),
    path('properties/', views.properties, name = "properties"),
    path('propertyViewMore/', views.propertyViewMore, name = "propertyViewMore"),
    # path('supprimerCategorie/', views.supprimerCategorie, name = "supprimerCategorie"),
    # path('supprimerProduit/', views.supprimerProduit, name = "supprimerProduit"),
    # path('vente/', views.vente, name = "vente"),
    # path('client/', views.client, name = "client"),
    # path('voirCategorie/', views.voirCategorie, name = "voirCategorie"),
    # path('recuDeVente/', views.recuDeVente, name = "recuDeVente"),
    # path('updateProduit/<int:pk>', views.updateProduit, name = "updateProduit"),
    # path('choixPayement/', views.choixPayement, name = "choixPayement"),
]