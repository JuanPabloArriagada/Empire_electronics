from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .listas import *

# Create your models here.
class Cliente(models.Model):
    rut = models.CharField(max_length=10, primary_key=True, null=False)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    telefono = models.IntegerField(validators=[MinValueValidator(10000000), MaxValueValidator(99999999)], null=False)
    correo = models.EmailField(null=False)
    direccion = models.CharField(max_length=100, null=False)
    numero_casa_depto = models.IntegerField(null=False)
    contraseña = models.CharField(max_length=50, null= False)

class Metodo_pago(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    nombre = models.CharField(max_length=50, choices=TIPO_PAGO, null=False)

class Marca(models.TextChoices):
    APPLE = 'APPLE', 'Apple'
    HP = 'HP', 'HP'
    SAMSUNG = 'SAMSUNG', 'Samsung'
    HUAWEI = 'HUAWEI', 'Huawei'

class Procesador(models.Model):
    modelo=models.CharField(max_length=50, primary_key=True, null=False)
    marca = models.CharField(max_length=50, null=False)
    generacion = models.CharField(max_length=50, null=False)

class Laptops(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    marca = models.CharField(max_length=50, choices=Marca.choices, null=False)
    modelo = models.CharField(max_length=50, null=False)
    pulgadas = models.FloatField(null=False, choices=TIPO_PULGADAS)
    resolucion = models.IntegerField(null=False, choices=TIPO_RESOLUCION)
    memoria_ram = models.IntegerField(null=False, choices=TIPO_RAM)
    bateria = models.IntegerField(null=False, choices=TIPO_BATERIA)
    almacenamiento = models.CharField(max_length=50 ,null=False, choices=TIPO_ALMACENAMIENTO_LAPTOPS, default='otro')
    tarjeta_video = models.CharField(max_length=50, choices=TIPO_TARJETA_VIDEO, null=False)
    procesador = models.ForeignKey(Procesador, on_delete=models.PROTECT)
    precio = models.FloatField(null=False)
    stock = models.IntegerField(null=False)
    estado = models.CharField(max_length=50, choices=TIPO_ESTADO_PRODUCTO, null=False)

class Celulares(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    marca = models.CharField(max_length=50, choices=Marca.choices, null=False)
    modelo = models.CharField(max_length=50, null=False)
    pulgadas = models.FloatField(null=False, choices=TIPO_PULGADAS)
    resolucion = models.IntegerField(null=False, choices=TIPO_RESOLUCION)
    bateria = models.IntegerField(null=False, choices=TIPO_BATERIA)
    almacenamiento = models.CharField(max_length=50, null=False, choices=TIPO_ALMACENAMIENTO_CELULAR, default='otro')
    camara = models.CharField(max_length=50, choices=TIPO_CAMARA, null=False)
    precio = models.FloatField(null=False)
    stock = models.IntegerField(null=False)
    estado = models.CharField(max_length=50, choices=TIPO_ESTADO_PRODUCTO, null=False)