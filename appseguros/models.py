from django.db import models

# Create your models here.
class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)

class Asegurado(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField()

class Vehiculo(models.Model):
    dominio = models.CharField(max_length=7)
    año = models.IntegerField()
    numero_motor = models.CharField(max_length=40)

class Tarea(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=5000)

class Siniestro(models.Model):
    numero_siniestro = models.CharField(max_length=30)
    asegurado = models.CharField(max_length=30)
    informacion = models.CharField(max_length=5000)
