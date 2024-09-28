from django.db import models

# Create your models here.

class Team(models.Model):
    nombre = models.CharField(max_length=200)
    capitan= models.CharField(max_length=200)
    descripcion= models.TextField(blank=True)
    jugadores=models.CharField(max_length=200)
    activo= models.BooleanField(default=False)
    
    def __str__(self) : #para acceder a la misma instancia del objeto 
        return self.nombre #para elpanel administrador

#que datos seran seleccionanos para enviarlos del backen en json para el front
#en django son serializados en objetos y luego son en querysets
#django -python-json #