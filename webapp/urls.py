from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),      
    path('contacto/', views.contacto, name="contacto"), 
    path('personas/', views.personas, name="personas"),      
    path('servicios/', views.servicios, name="servicios"),
    path('detalle/<int:id>', views.detalle, name="detalle"),         
]     






