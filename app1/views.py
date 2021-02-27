import random
import csv

from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required

import uuid
# Create your views here.
def inicio(request):
    print("COOKIES RECIBIDAS: ", request.COOKIES['identificador'])
    lista_nombres=["jhonn","elias","sara conor","blade", "van helsing","freddy", "jason"]
    context = {'temperatura': random.randint(10,32), 'nombres':lista_nombres}
    response = render(request,'app1/index.html', context)
    if not ('identificador' in request.COOKIES.keys()):
        max_age = 365 * 24 * 60 * 60  # 1 Año
        response.set_cookie(
                        key="identificador", 
                        value=uuid.uuid4(), 
                        max_age=max_age
                        )
    return response

@login_required(login_url="/accounts/login/")
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
    print(dict(request.session))
    if 'num_visitas' not in request.session:
        request.session['num_visitas']= 1
    else:
        request.session['num_visitas'] += 1
    context['num_visitas']=request.session['num_visitas']
    return render(request, 'app1/datos.html', context)



def map(request):
    return render(request, 'app1/map.html')