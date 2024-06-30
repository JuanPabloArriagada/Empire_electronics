from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

#CLIENTE FORMS
class ClienteForm(UserCreationForm):
    rut=forms.CharField(max_length=10, error_messages={"required":"Ingrese rut sin puntos y con guión ej.:12345678-9"}, help_text="Debe ingresar rut")

    class Meta(UserCreationForm.Meta):
        model = Cliente
        fields = ['rut','nombre', 'apellido', 'correo', 'telefono','fecha_ncto' , 'direccion']

class UpdateClienteForm(UserChangeForm):
    fecha_ncto=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta(UserChangeForm.Meta):
        model = Cliente
        fields = ('rut', 'nombre', 'apellido', 'correo', 'telefono', 'fecha_ncto', 'direccion')

#ADMIN FORM
class AdminCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['rut', 'correo', 'password']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_staff = True
        if commit:
            user.save()
        return user



#PRODUCTO FORM
class ProductoForm(forms.ModelForm):
    marca = forms.ChoiceField(choices=Marca.choices)
    modelo = forms.CharField(max_length=50)
    precio = forms.IntegerField()
    stock = forms.IntegerField()
    estado = forms.ChoiceField(choices=TIPO_ESTADO_PRODUCTO)

    class Meta:
        model = Producto
        fields = ['marca', 'modelo', 'precio', 'stock', 'estado']



#LAPTOPS FORMS
class LaptopsForm(forms.ModelForm):
    class Meta:
        model = Laptops
        fields = '__all__'


#CELULARES FORMS
class CelularesForm(forms.ModelForm):
    class Meta:
        model = Celulares
        fields = '__all__'

#CARRITO
class CartAddProductForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity']

class CartUpdateProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)