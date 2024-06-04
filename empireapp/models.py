from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .listas import *

# Create your models here.
class Cliente(models.Model):
    rut=models.CharField(max_length=10, primary_key=True, null=False)
    nombre=models.CharField(max_length=50, null=False)
    apellido=models.CharField(max_length=50, null=False)
    correo=models.EmailField(error_messages='Ta mal el correo')
    telefono=models.IntegerField(validators=[MinValueValidator(10000000), MaxValueValidator(99999999)])
    #region=models.CharField( default=" ")
    #comuna=models.CharField( default=" ")
    #ciudad=