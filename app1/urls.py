from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio,name='inicio'),
    path('empresa/', views.empresa,name='empresa'),
    path('contacto/', views.contacto,name='contacto'),
]