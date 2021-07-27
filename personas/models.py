from django.db import models
from django.db.models.deletion import SET_NULL

class Domicilio(models.Model):
    calle = models.CharField(max_length=100)
    altura = models.IntegerField(max_length=10)
    pais= models.CharField(max_length=100)

    def __str__(self):
        return f'Domicilio {self.id}: {self.calle} {self.altura} {self.pais}'

class Persona(models.Model):

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return  f'Persona {self.id}: {self.nombre} {self.apellido}'



