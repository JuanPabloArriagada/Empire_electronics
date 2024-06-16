from django import forms
from .models import *

class ClienteForm(forms.ModelForm):
    rut=forms.CharField(max_length=10, error_messages={"required":"Ingrese rut sin puntos y con guión ej.:12345678-9"}, help_text="Debe ingresar rut")

    class Meta:
        model = Cliente
        fields = ['rut','nombre', 'apellido','telefono', 'correo', 'direccion','numero_casa_depto','contraseña']


class LaptopsForm(forms.ModelForm):
    class Meta:
        model = Laptops
        fields = ['marca', 'modelo', 'pulgadas', 'resolucion', 'memoria_ram', 'bateria', 'almacenamiento', 'tarjeta_video', 'procesador', 'precio', 'stock']

class CarritoForm(forms.ModelForm):
    class Meta:
        model = Carrito
        fields = ['cliente', 'producto', 'cantidad']