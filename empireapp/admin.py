from django.contrib import admin
from .models import *

# Register your models here.

class AdmCliente(admin.ModelAdmin):
    list_display = ['rut', 'nombre', 'apellido', 'telefono', 'correo', 'direccion', 'fecha_ncto']
    list_editable = ['nombre', 'apellido', 'telefono', 'correo', 'direccion', 'fecha_ncto']
    list_display_links = None  # Evitar enlaces en la lista para permitir que los campos list_editable funcionen correctamente

class AdmLaptops(admin.ModelAdmin):
    list_display = ['pulgadas', 'resolucion', 'memoria_ram', 'bateria', 'almacenamiento', 'tarjeta_video', 'procesador']

class AdmCelulares(admin.ModelAdmin):
    list_display = ['pulgadas', 'resolucion', 'bateria', 'almacenamiento', 'camara']


admin.site.register(Cliente, AdmCliente)
admin.site.register(Laptops, AdmLaptops)
admin.site.register(Celulares, AdmCelulares)
