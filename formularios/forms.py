import datetime

from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

def validar_fecha(fecha):
    fecha_menor = datetime.datetime.strptime("2020-12-01", "%Y-%m-%d").date()
    fecha_mayor = datetime.datetime.strptime("2020-12-31", "%Y-%m-%d").date()
    if fecha_menor <= fecha <= fecha_mayor:
        return fecha
    else:
        raise ValidationError("Sólo acepta fechas de diciembre 2020")


class FormularioGuitarra(forms.Form):
    marca = forms.CharField(
                validators = [ 
                        validators.MinLengthValidator( 3, 
						    "La marca no puede ser de menos de 3 letras"),
                        validators.MaxLengthValidator( 10, 
						    "La marca no puede ser de más de 10 letras") ])   
    modelo = forms.CharField(
                validators = [ 
                        validators.MinLengthValidator( 3, 
						    "El modelo no puede ser de menos de 3 letras"),
                        validators.MaxLengthValidator( 10, 
						    "La modelo no puede ser de más de 10 letras") ])
    cuerdas = forms.IntegerField(validators = [ 
                        validators.MinValueValidator( 6, 
						    "No pueden ser menos de 6 cuerdas"),
                        validators.MaxValueValidator( 12, 
						    "No pueden ser más de 12 cuerdas") ])
    fecha_compra = forms.DateField(validators = [validar_fecha])
