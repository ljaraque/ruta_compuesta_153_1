from django.urls import path
from . import views

app_name = "app1"

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('empresa/', views.empresa,name='empresa'),
    path('contacto/', views.contacto,name='contacto'),
    path('datos/', views.datos, name='datos')
]