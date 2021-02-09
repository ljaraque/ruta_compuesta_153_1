from django.urls import path
from . import views

app_name = "formularios"

urlpatterns = [
    path('crear_guitarra', views.crear_guitarra, name='crear_guitarra'),
    path(
        'crear_guitarra_exitoso', 
        views.crear_guitarra_exitoso, 
        name='crear_guitarra_exitoso'
        ),
    path('graficos/', views.grafico, name='graficos')
]