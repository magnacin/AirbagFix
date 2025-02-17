
from django.urls import path
from . import views

# Creamos un url para cada vista de la pagina

urlpatterns = [
    path('', views.home, name = "home"),
    path('airbag/', views.airbag, name = "airbag"),
    path('archivos/', views.archivos, name = "archivos"),
    path('dpf/', views.dpf, name = "dpf"),
    path('contacts/', views.contacts, name = "contacts"), # puede ser tambien en lugar de /contacts
    path('leer/', views.leer, name = "leer"), # contacts.html o cualquier pagina
]