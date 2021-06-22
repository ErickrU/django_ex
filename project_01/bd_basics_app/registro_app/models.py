from django.db import models
from django.db.models.manager import Manager

# Create your models here.
class Grupo(models.Model):
    tittle =  models.CharField(max_length=50)

    def __str__(self):
        return self.tittle

class alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    no_control = models.CharField(max_length=10)
    cuatrimestres = models.CharField(max_length=5)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    