from django.contrib import admin
from .models import Perfil

# Register your models here.

class PerfilAdmin(admin.ModelAdmin):
    fields = ['usuario','descripcion', 'nacionalidad', 'altura', 'peso', 'codigo_postal', 'archivo_foto','rol', 'direccion'] # campos para edicion
    list_display=('usuario','descripcion', 'rol', 'peso', 'altura', 'direccion', 'codigo_postal') # campos para lista
    list_filter = ['peso', 'altura']
    search_fields = ['descripcion', 'rol', 'direccion']

admin.site.register(Perfil, PerfilAdmin)