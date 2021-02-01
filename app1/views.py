from django.shortcuts import render
import random

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



