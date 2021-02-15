import json
import datetime

from django.shortcuts import render, redirect
from .forms import FormularioGuitarra
from django.conf import settings
from .models import Guitarra


def context_lista_guitarras():
    filename= "/formularios/data/guitarras.json"
    with open(str(settings.BASE_DIR)+filename, 'r') as file:
        guitarras=json.load(file)
    
    # ordenar con funcion convencional
    def criterio_ordenamiento(diccionario):
        return diccionario['identificador']
    guitarras['guitarras'] = sorted(guitarras['guitarras'], key=criterio_ordenamiento)
    '''
    # ordenar con lambda function
    guitarras['guitarras'] = sorted(guitarras['guitarras'], key=lambda k: k['identificador'])
    '''
    print(guitarras['guitarras'])
    context = {'lista_guitarras': guitarras['guitarras']}
    return context

# Create your views here.

# C de CRUD con archivo JSON
def crear_guitarra(request):

    if request.method == "GET":
        formulario = FormularioGuitarra()
        context = {'formulario': formulario}
        context.update(context_lista_guitarras())
        print(context)
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
                data=json.load(file)
                nuevo_ultimo_identificador = int(data['ultimo_identificador']) + 1
                data['ultimo_identificador'] = nuevo_ultimo_identificador
                datos_formulario['identificador'] = nuevo_ultimo_identificador
                data['guitarras'].append(datos_formulario)
            with open(str(settings.BASE_DIR)+filename, 'w') as file:
                json.dump(data, file)
            
            return redirect('formularios:crear_guitarra')
        else:
            context = {'formulario': formulario_devuelto}
            context.update(context_lista_guitarras())
            return render(request, 'formularios/crear_guitarra.html', context)


# R de CRUD con archivo JSON
def lista_guitarras(request):
    context = context_lista_guitarras()
    return render(request, 'formularios/lista_guitarras.html', context)

# U de CRUD con archivo JSON
def editar_guitarra(request, identificador):

    if request.method == "GET":
        filename= "/formularios/data/guitarras.json"
        with open(str(settings.BASE_DIR)+filename, 'r') as file:
            data=json.load(file)
        for guitarra in data['guitarras']:
            if int(guitarra['identificador'])==int(identificador):
                break
        formulario = FormularioGuitarra(initial=guitarra)
        context = {'formulario': formulario, 'identificador': identificador}
        return render(request, 'formularios/editar_guitarra.html', context)

    elif request.method == "POST":
        print("El POST contiene:", request.POST)
        formulario_devuelto = FormularioGuitarra(request.POST)
        if formulario_devuelto.is_valid() == True:
            datos_formulario = formulario_devuelto.cleaned_data
            datos_formulario['fecha_compra']=datos_formulario['fecha_compra'].strftime("%Y-%m-%d")
            filename= "/formularios/data/guitarras.json"
            with open(str(settings.BASE_DIR)+filename, 'r') as file:
                data=json.load(file)
            for guitarra in data['guitarras']:
                if int(guitarra['identificador'])==int(identificador):
                    data['guitarras'].remove(guitarra)
                    datos_formulario['identificador'] = guitarra['identificador']
                    data['guitarras'].append(datos_formulario)
                    break
            with open(str(settings.BASE_DIR)+filename, 'w') as file:
                json.dump(data, file)
            return redirect('formularios:lista_guitarras')
        else:
            context = {'formulario': formulario_devuelto}
            return render(request, 'formularios/editar_guitarra.html', context)


# D de CRUD con archivo JSON
def eliminar_guitarra(request, identificador):

    if request.method == "GET":
        context = {'identificador': identificador}
        return render(request, "formularios/eliminar_guitarra.html", context)

    if request.method == "POST":
        filename= "/formularios/data/guitarras.json"
        with open(str(settings.BASE_DIR)+filename, 'r') as file:
            data=json.load(file)
        for guitarra in data['guitarras']:
            if int(guitarra['identificador'])==int(identificador):
                data['guitarras'].remove(guitarra)
                break
        with open(str(settings.BASE_DIR)+filename, 'w') as file:
            json.dump(data, file)
        
        return redirect('formularios:lista_guitarras')


# C de CRUD con Base de Datos
'''
# EN DESARROLLO
def crear_guitarra_db(request):

    if request.method == "GET":
        formulario = FormularioGuitarra()
        context = {'formulario': formulario}
        context.update(context_lista_guitarras())
        print(context)
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
                data=json.load(file)
                nuevo_ultimo_identificador = int(data['ultimo_identificador']) + 1
                data['ultimo_identificador'] = nuevo_ultimo_identificador
                datos_formulario['identificador'] = nuevo_ultimo_identificador
                data['guitarras'].append(datos_formulario)
            with open(str(settings.BASE_DIR)+filename, 'w') as file:
                json.dump(data, file)
            
            return redirect('formularios:crear_guitarra')
        else:
            context = {'formulario': formulario_devuelto}
            context.update(context_lista_guitarras())
            return render(request, 'formularios/crear_guitarra.html', context)
'''


# R de CRUD con Base de Datos

# U de CRUD con Base de Datos

# D de CRUD con Base de Datos






def grafico(request):
    lista_cuerdas = []
    lista_modelo = []
    filename= "/formularios/data/guitarras.json"
    with open(str(settings.BASE_DIR)+filename, 'r') as file:
        lista_guitarras = json.load(file) 
        for elemento in lista_guitarras.get('guitarras')[-5:]:
            cuerdas = elemento.get('cuerdas')
            modelo = elemento.get('modelo')
            lista_cuerdas.append(cuerdas)
            lista_modelo.append(modelo)
    print(lista_cuerdas)
    print(lista_modelo)
    context = {'cuerdas':lista_cuerdas, 'modelos':lista_modelo}
    return render(request, 'formularios/graficos.html', context)


def prueba_models(request):
    context = {'guitarras':Guitarra.objects.all(),
               'guitarras_values': Guitarra.objects.values()}
    print(context)
    return render(request, 'formularios/prueba_models.html', context)

