import datetime
from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError


def validar_fecha(fecha):
    fecha_menor = datetime.datetime.strptime("2020-12-01", "%Y-%m-%d").date()
    fecha_mayor = datetime.datetime.strptime("2020-12-31", "%Y-%m-%d").date()
    if fecha_menor <= fecha <= fecha_mayor:
        return fecha
    else:
        raise ValidationError("Sólo acepta fechas de diciembre 2020")


# Create your models here.

class Musico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    pais = models.CharField(max_length=50, default="Chile")

class Guitarra(models.Model):
    marca = models.CharField(max_length=80)
    modelo = models.CharField(max_length=80)
    cuerdas = models.IntegerField()
    madera = models.CharField(max_length=50, default="No informada")
    fecha_compra = models.DateField()
    musico = models.ForeignKey(Musico, on_delete=models.CASCADE)

class Banda(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_formacion = models.DateField()
    musicos = models.ManyToManyField(Musico)

'''
class pasaporte(models.Model):
    numero = models.IntegerField()
    musico = models.OneToOneField(Musico, on_delete=models.CASCADE)

'''

# Modelo de Guitarra para vistas basadas en clases (CBV)

class GuitarraCBV(models.Model):
    marca = models.CharField(max_length=80,
                validators = [ 
                        validators.MinLengthValidator( 3, 
						    "La marca no puede ser de menos de 3 letras"),
                        validators.MaxLengthValidator( 10, 
						    "La marca no puede ser de más de 10 letras") ]
                )
    modelo = models.CharField(max_length=80,
                validators = [ 
                        validators.MinLengthValidator( 3, 
						    "El modelo no puede ser de menos de 3 letras"),
                        validators.MaxLengthValidator( 30, 
						    "El modelo no puede ser de más de 30 letras") ]
                )
    cuerdas = models.IntegerField(
                validators = [ 
                        validators.MinValueValidator( 6, 
						    "No pueden ser menos de 6 cuerdas"),
                        validators.MaxValueValidator( 12, 
						    "No pueden ser más de 12 cuerdas") ]
                )
    madera = models.CharField(max_length=50, default="No informada")
    fecha_compra = models.DateField(validators = [validar_fecha])
