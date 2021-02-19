from django.urls import path
from . import views

app_name = "formularios"

urlpatterns = [
    path('crear_guitarra', views.crear_guitarra, name='crear_guitarra'),
    path('crear_guitarra_db', views.crear_guitarra_db, name='crear_guitarra_db'),
    path('lista_guitarras', views.lista_guitarras, name='lista_guitarras'),
    path('lista_guitarras_db', views.lista_guitarras_db, name='lista_guitarras_db'),
    path('<identificador>/borrar_guitarra', views.eliminar_guitarra, name='eliminar_guitarra'),
    path('<identificador>/borrar_guitarra_db', views.eliminar_guitarra_db, name='eliminar_guitarra_db'),
    path('<identificador>/editar_guitarra', views.editar_guitarra, name='editar_guitarra'),
    path('<identificador>/editar_guitarra_db', views.editar_guitarra_db, name='editar_guitarra_db'),
    path('graficos/', views.grafico, name='graficos'),
    path('prueba_models/', views.prueba_models, name="prueba_models"),
    path('lista_guitarras_db_cbv', views.ListaGuitarras.as_view(), name='lista_guitarras_db_cbv'),
    path('crear_guitarra_db_cbv', views.CrearGuitarra.as_view(), name='crear_guitarra_db_cbv'),

]
