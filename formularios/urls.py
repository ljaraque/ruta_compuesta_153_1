from django.urls import path
from . import views

app_name = "formularios"

urlpatterns = [
    path('crear_guitarra', views.crear_guitarra, name='crear_guitarra'),
    path('lista_guitarras', views.lista_guitarras, name='lista_guitarras'),
    path('<identificador>/borrar_guitarra', views.eliminar_guitarra, name='eliminar_guitarra'),
    path('<identificador>/editar_guitarra', views.editar_guitarra, name='editar_guitarra'),
    path('graficos/', views.grafico, name='graficos'),
    path('prueba_models/', views.prueba_models, name="prueba_models")

]
