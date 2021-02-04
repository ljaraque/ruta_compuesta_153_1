import json
import datetime

from django.shortcuts import render
from .forms import FormularioGuitarra
from django.conf import settings

# Create your views here.

def crear_guitarra(request):

    if request.method == "GET":
        formulario = FormularioGuitarra()
        context = {'formulario': formulario}
        return render(request, 'formularios/crear_guitarra.html', context)

    elif request.method == "POST":
        print("El POST contiene:", request.POST)

        formulario_devuelto = FormularioGuitarra(request.POST)

        if formulario_devuelto.is_valid() == True:
            datos_formulario = formulario_devuelto.cleaned_data
            datos_formulario['fecha_compra']=datos_formulario['fecha_compra'].strftime("%Y-%m-%d")
            print("Los datos limpios del formulario son:", datos_formulario)
            filename= "/formularios/data/guitarras.json"
            with open(str(settings.BASE_DIR)+filename, 'r') as file:
                guitarras=json.load(file)
                guitarras['guitarras'].append(datos_formulario)
            with open(str(settings.BASE_DIR)+filename, 'w') as file:
                json.dump(guitarras, file)
            context = {'lista_guitarras': guitarras['guitarras']}
            return render(request, 'formularios/crear_guitarra_exitoso.html', context)
        else:
            context = {'formulario': formulario_devuelto}
            return render(request, 'formularios/crear_guitarra.html', context)


def crear_guitarra_exitoso(request):
    guitarras = []
    context = {'guitarras': guitarras}
    return render(request, 'formularios/crear_guitarra_exitoso.html', context)