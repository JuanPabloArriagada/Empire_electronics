from django.contrib import admin
from .models import *

# Register your models here.
class AdmCliente(admin.ModelAdmin):
    list_display = ['rut', 'nombre', 'apellido', 'telefono', 'correo', 'direccion', 'numero_casa_depto', 'contraseña']
    list_editable = ['nombre', 'apellido', 'telefono', 'correo', 'direccion', 'numero_casa_depto', 'contraseña']
    list_display_links = None  # Evitar enlaces en la lista para permitir que los campos list_editable funcionen correctamente

class AdmLaptops(admin.ModelAdmin):
    list_display = ['id', 'marca', 'modelo', 'pulgadas', 'resolucion', 'memoria_ram', 'bateria', 'almacenamiento', 'tarjeta_video', 'procesador', 'precio', 'stock']
    list_editable = ['marca','modelo', 'pulgadas', 'resolucion', 'memoria_ram', 'bateria', 'almacenamiento', 'tarjeta_video', 'procesador', 'precio', 'stock']

class AdmCelulares(admin.ModelAdmin):
    list_display = ['id', 'marca', 'modelo', 'pulgadas', 'resolucion', 'bateria', 'almacenamiento', 'camara', 'precio', 'stock']
    list_editable = ['modelo', 'pulgadas', 'resolucion', 'bateria', 'almacenamiento', 'camara', 'precio', 'stock']

class AdmCarrito(admin.ModelAdmin):
    list_display = ['cliente', 'producto', 'cantidad']
    list_editable = ['cantidad']


admin.site.register(Cliente, AdmCliente)
admin.site.register(Laptops, AdmLaptops)
admin.site.register(Celulares, AdmCelulares)
admin.site.register(Carrito, AdmCarrito)