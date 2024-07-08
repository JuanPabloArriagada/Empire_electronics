from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from datetime import date


#CLIENTE FORMS
class ClienteForm(UserCreationForm):
    rut = forms.CharField(
        max_length=10,
        error_messages={"required": "Ingrese rut sin puntos y con guión ej.: 12345678-9"},
        help_text="Debe ingresar rut"
    )
    correo = forms.EmailField(validators=[validate_email])
    telefono = forms.IntegerField()
    fecha_ncto = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta(UserCreationForm.Meta):
        model = Cliente
        fields = ['rut', 'nombre', 'apellido', 'correo', 'telefono', 'fecha_ncto', 'direccion']

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if int(rut) <= 10000000 and int(rut) >= 999999999:
            raise ValidationError("El RUT debe estar entre 10000000 y 99999999.")
        return rut

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if int(telefono) <= 10000000 and int(telefono) >= 999999999:
            raise ValidationError("El teléfono debe estar entre 10000000 y 99999999.")
        return telefono

    def clean_fecha_ncto(self):
        fecha_ncto = self.cleaned_data.get('fecha_ncto')
        today = date.today()
        age = today.year - fecha_ncto.year - ((today.month, today.day) < (fecha_ncto.month, fecha_ncto.day))
        if age < 15:
            raise ValidationError("Debe tener al menos 15 años.")
        return fecha_ncto

class UpdateClienteForm(UserChangeForm):
    fecha_ncto = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    password = forms.CharField(label='Contraseña', strip=False, required=False, widget=forms.PasswordInput)
    correo = forms.EmailField(validators=[validate_email])
    telefono = forms.IntegerField()

    class Meta(UserChangeForm.Meta):
        model = Cliente
        fields = ('rut', 'nombre', 'apellido', 'correo', 'telefono', 'fecha_ncto', 'direccion')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rut'].disabled = True  # Deshabilita el campo rut

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:
            # Validación adicional si es necesario
            # Puedes agregar validaciones personalizadas para la contraseña aquí
            pass  # Por ejemplo, longitud mínima, caracteres especiales, etc.
        return password

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if not (10000000 <= telefono <= 99999999):
            raise ValidationError("El teléfono debe estar entre 10000000 y 99999999.")
        return telefono

    def clean_fecha_ncto(self):
        fecha_ncto = self.cleaned_data.get('fecha_ncto')
        today = date.today()
        age = today.year - fecha_ncto.year - ((today.month, today.day) < (fecha_ncto.month, fecha_ncto.day))
        if age < 15:
            raise ValidationError("Debe tener al menos 15 años.")
        return fecha_ncto

    def save(self, commit=True):
        instance = super().save(commit=False)
        password = self.cleaned_data['password']
        if password:
            instance.set_password(password)
        if commit:
            instance.save()
        return instance

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