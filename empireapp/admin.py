from django.contrib import admin
from .models import *

# Register your models here.
class AdmCliente(admin.ModelAdmin):
    list_display = ['rut', 'nombre', 'apellido', 'telefono', 'correo', 'direccion', 'numero_casa_depto', 'contraseña']
    list_editable = ['nombre', 'apellido', 'telefono', 'correo', 'direccion', 'numero_casa_depto', 'contraseña']
    list_display_links = None  # Evitar enlaces en la lista para permitir que los campos list_editable funcionen correctamente

class AdmMetodo_pago(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    list_editable = ['nombre']

class AdmProcesador(admin.ModelAdmin):
    list_display = ['marca', 'generacion']
    list_editable = ['marca']
    list_display_links = None  # Si lo necesitas, aquí también puedes deshabilitar los enlaces en la lista


class AdmLaptops(admin.ModelAdmin):
    list_display = ['id', 'marca', 'modelo', 'pulgadas', 'resolucion', 'memoria_ram', 'bateria', 'almacenamiento', 'tarjeta_video', 'procesador', 'precio', 'stock', 'estado']
    list_editable = ['modelo', 'pulgadas', 'resolucion', 'memoria_ram', 'bateria', 'almacenamiento', 'tarjeta_video', 'procesador', 'precio', 'stock', 'estado']

class AdmCelulares(admin.ModelAdmin):
    list_display = ['id', 'marca', 'modelo', 'pulgadas', 'resolucion', 'bateria', 'almacenamiento', 'camara', 'precio', 'stock', 'estado']
    list_editable = ['modelo', 'pulgadas', 'resolucion', 'bateria', 'almacenamiento', 'camara', 'precio', 'stock', 'estado']

admin.site.register(Cliente, AdmCliente)
admin.site.register(Metodo_pago, AdmMetodo_pago)
admin.site.register(Procesador, AdmProcesador)
admin.site.register(Laptops, AdmLaptops)
admin.site.register(Celulares, AdmCelulares)