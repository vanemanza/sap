from django.shortcuts import render
from personas.models import *

def home(request):

    return render(request, 'webapp/home.html')


def contacto(request):

    return render(request, 'webapp/Contacto.html')


def personas(request):

    personas = Persona.objects.all()
    cantidad = Persona.objects.count()
    context = {'personas': personas, 'cantidad': cantidad}
    return render(request, 'webapp/personas.html', context)


def servicios(request):

    return render(request, 'webapp/servicios.html')        


def detalle(request, id):
    info = Persona.objects.get(id=id)
    return render(request, 'webapp/detalle.html', {'info': info})         