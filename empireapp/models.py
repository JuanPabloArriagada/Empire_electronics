
import uuid
from django.db import models
from .listas import *
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.
class ClienteManager(BaseUserManager):
    def create_user(self, rut, nombre, apellido, correo, telefono, fecha_ncto, direccion, password=None):
        if not correo:
            raise ValueError('El usuario debe tener un correo electrónico')
        user = self.model(
            rut=rut,
            nombre=nombre,
            apellido=apellido,
            correo=self.normalize_email(correo),
            telefono=telefono,
            fecha_ncto=fecha_ncto,
            direccion=direccion
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, rut, nombre, apellido, correo, telefono, fecha_ncto, direccion, password=None):
        user = self.create_user(
            rut=rut,
            nombre=nombre,
            apellido=apellido,
            correo=correo,
            telefono=telefono,
            fecha_ncto=fecha_ncto,
            direccion=direccion,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Cliente(AbstractBaseUser, PermissionsMixin):
    rut = models.CharField(max_length=12, unique=True, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100, unique=True)
    telefono = models.CharField(max_length=20)
    fecha_ncto = models.DateField(default=timezone.now)
    direccion = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = ClienteManager()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['rut', 'nombre', 'apellido', 'telefono', 'fecha_ncto', 'direccion']

    def __str__(self):
        return f"RUT:{self.rut} NOMBRE: {self.nombre} {self.apellido}"

class Marca(models.TextChoices):
    APPLE = 'APPLE', 'Apple'
    HP = 'HP', 'HP'
    SAMSUNG = 'SAMSUNG', 'Samsung'
    HUAWEI = 'HUAWEI', 'Huawei'
    

class Producto(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    marca = models.CharField(max_length=50, choices=Marca.choices, null=False)
    modelo = models.CharField(max_length=50, null=False)
    precio = models.PositiveIntegerField(null=False)
    stock = models.PositiveIntegerField(null=False)
    estado = models.CharField(max_length=50, choices=TIPO_ESTADO_PRODUCTO)


    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return f"ID: {self.id} MARCA: {self.marca} MODELO: {self.modelo} PRECIO: {self.precio} STOCK: {self.stock}"

class Laptops(Producto):
    imagen = models.ImageField(upload_to='laptops', null=True)
    pulgadas = models.FloatField(null=False, choices=TIPO_PULGADAS)
    resolucion = models.IntegerField(null=False, choices=TIPO_RESOLUCION)
    memoria_ram = models.IntegerField(null=False, choices=TIPO_RAM)
    bateria = models.IntegerField(null=False, choices=TIPO_BATERIA)
    almacenamiento = models.CharField(max_length=50, null=False, choices=TIPO_ALMACENAMIENTO_LAPTOPS, default='otro')
    tarjeta_video = models.CharField(max_length=50, choices=TIPO_TARJETA_VIDEO, null=False)
    procesador = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Laptop'
        verbose_name_plural = 'Laptops'

    def __str__(self):
        return f"Laptop - {self.marca} {self.modelo}"

class Celulares(Producto):
    imagen = models.ImageField(upload_to='celulares')
    pulgadas = models.FloatField(null=False, choices=TIPO_PULGADAS)
    resolucion = models.IntegerField(null=False, choices=TIPO_RESOLUCION)
    bateria = models.IntegerField(null=False, choices=TIPO_BATERIA)
    almacenamiento = models.CharField(max_length=50, null=False, choices=TIPO_ALMACENAMIENTO_CELULAR, default='otro')
    camara = models.CharField(max_length=50, choices=TIPO_CAMARA, null=False)

    class Meta:
        verbose_name = 'Celular'
        verbose_name_plural = 'Celulares'

    def __str__(self):
        return f"Celular - {self.marca} {self.modelo}"

#CARRITO
User = get_user_model()

class Cart(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cart {self.id} for {self.user.email}'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.producto.nombre}'