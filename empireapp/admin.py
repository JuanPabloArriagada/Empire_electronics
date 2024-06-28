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

class AdmCart(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__rut', 'user__nombre', 'user__apellido']

class AdmCartItem(admin.ModelAdmin):
    list_display = ['cart', 'producto', 'quantity']

admin.site.register(Cliente, AdmCliente)
admin.site.register(Laptops, AdmLaptops)
admin.site.register(Celulares, AdmCelulares)
admin.site.register(Cart, AdmCart)
admin.site.register(CartItem, AdmCartItem)