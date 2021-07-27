from django.urls import path
from . import views


urlpatterns = [
    path('', views.personas, name="personas"),   
    path('personas/', views.personas, name="personas"),  
    path('detalle/<id>', views.detalle, name="detalle"),  
    
]




