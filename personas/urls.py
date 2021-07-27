from django.urls import path
from . import views


urlpatterns = [ 
    path('detalle/<id>', views.detalle, name="detalle"),      
]




