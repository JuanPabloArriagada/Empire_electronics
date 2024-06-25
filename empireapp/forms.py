from django import forms
from .models import *

#CLIENTE FORMS
class ClienteForm(forms.ModelForm):
    rut=forms.CharField(max_length=10, error_messages={"required":"Ingrese rut sin puntos y con guión ej.:12345678-9"}, help_text="Debe ingresar rut")

    class Meta:
        model = Cliente
        fields = ['rut','nombre', 'apellido','telefono', 'correo', 'direccion','fecha_ncto']

class UpdateClienteForm(forms.ModelForm):
    fecha_ncto=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Cliente
        fields = ['rut','nombre', 'apellido','telefono', 'correo', 'direccion','fecha_ncto']


#LAPTOPS FORMS
class LaptopsForm(forms.ModelForm):
    class Meta:
        model = Laptops
        fields = ['imagen','marca', 'modelo', 'pulgadas', 'resolucion', 'memoria_ram', 'bateria', 'almacenamiento', 'tarjeta_video', 'procesador', 'precio', 'stock']

class UpdateLaptopsForm(forms.ModelForm):
    
    class Meta:
        model = Laptops
        fields = ['imagen','marca','modelo', 'pulgadas', 'resolucion', 'memoria_ram', 'bateria', 'almacenamiento', 'tarjeta_video', 'procesador', 'precio', 'stock']


#CELULARES FORMS
class CelularesForms(forms.ModelForm):
    class Meta:
        model = Celulares
        fields = ['imagen','marca', 'modelo', 'pulgadas', 'resolucion', 'bateria', 'almacenamiento', 'camara', 'precio', 'stock']


class UpdateCelularesForm(forms.ModelForm):
    
    class Meta:
        model = Celulares
        fields = ['imagen','marca', 'modelo', 'pulgadas', 'resolucion', 'bateria', 'almacenamiento', 'camara', 'precio', 'stock']


#CARRITO
class CarritoForm(forms.ModelForm):
    class Meta:
        model = Carrito
        fields = ['cliente', 'producto', 'cantidad']