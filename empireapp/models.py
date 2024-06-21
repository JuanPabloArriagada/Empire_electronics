from datetime import date
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .listas import *

# Create your models here.
class Cliente(models.Model):
    rut = models.CharField(max_length=12, unique=True, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=20)
    fecha_ncto = models.DateField(default=date.today)
    direccion = models.CharField(max_length=255)
    
    def __str__(self):
        return f"RUT:{self.rut} NOMBRE: {self.nombre} {self.apellido}"

class Marca(models.TextChoices):
    APPLE = 'APPLE', 'Apple'
    HP = 'HP', 'HP'
    SAMSUNG = 'SAMSUNG', 'Samsung'
    HUAWEI = 'HUAWEI', 'Huawei'
    

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
    procesador = models.CharField(max_length=50, null=False)
    precio = models.PositiveIntegerField(null=False)
    stock = models.PositiveIntegerField(null=False)
    
    def __str__(self):
        return f"ID:{self.id} MARCA: {self.marca} {self.modelo}"

class Celulares(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    marca = models.CharField(max_length=50, choices=Marca.choices, null=False)
    modelo = models.CharField(max_length=50, null=False)
    pulgadas = models.FloatField(null=False, choices=TIPO_PULGADAS)
    resolucion = models.IntegerField(null=False, choices=TIPO_RESOLUCION)
    bateria = models.IntegerField(null=False, choices=TIPO_BATERIA)
    almacenamiento = models.CharField(max_length=50, null=False, choices=TIPO_ALMACENAMIENTO_CELULAR, default='otro')
    camara = models.CharField(max_length=50, choices=TIPO_CAMARA, null=False)
    precio = models.PositiveIntegerField(null=False)
    stock = models.PositiveIntegerField(null=False)
    
    def __str__(self):
        return f"ID:{self.id} MARCA: {self.marca} {self.modelo}"

class Carrito(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Laptops, on_delete=models.CASCADE)  # Change to a more generic model if needed
    cantidad = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('cliente', 'producto')

    def __str__(self):
        return f"Cliente: {self.cliente.rut}, Producto: {self.producto.marca} {self.producto.modelo}, Cantidad: {self.cantidad}"

    def agregar_producto(self, producto_id):
        # Logic to add product and increment quantity if already exists
        carrito_item, created = Carrito.objects.get_or_create(cliente=self.cliente, producto_id=producto_id)
        if not created:
            carrito_item.cantidad += 1
            carrito_item.save()