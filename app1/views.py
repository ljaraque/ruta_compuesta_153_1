import random
import csv

from django.shortcuts import render
from django.conf import settings


# Create your views here.
def inicio(request):
    lista_nombres=["jhonn","elias","sara conor","blade", "van helsing","freddy", "jason"]
    context = {'temperatura': random.randint(10,32), 'nombres':lista_nombres}
    return render(request,'app1/index.html', context)

def empresa(request):
    context = {'temperatura': random.randint(10,32)}
    return render(request,'app1/empresa.html', context)

def contacto(request):
    context = {'temperatura': random.randint(10,32)}
    return render(request,'app1/contacto.html', context)

def datos(request):
    filename = '/app1/data/iris.csv'
    ruta_completa_archivo = str(settings.BASE_DIR)+filename
    with open(ruta_completa_archivo, 'r') as archivo:
        data = csv.DictReader(archivo)
        data_list = []
        for elemento in data:
            data_list.append(elemento)

    context = {'datos_desde_archivo': data_list}
    return render(request, 'app1/datos.html', context)



