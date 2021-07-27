from django.shortcuts import render
from .models import Persona
# Create your views here.

def detalle(request, id):
    persona = Persona.objects.get(pk=id)
    return render(request, 'personas/detalle.html', {'persona': persona})   

