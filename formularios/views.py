from django.shortcuts import render
from .forms import FormularioGuitarra

# Create your views here.

def crear_guitarra(request):
    formulario = FormularioGuitarra()
    context = {'formulario': formulario}
    return render(request, 'formularios/crear_guitarra.html', context)