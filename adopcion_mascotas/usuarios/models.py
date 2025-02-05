from django.db import models
from direcciones.models import Direcciones

# Create your models here.
class Usuario(models.Model):
	nombre=models.CharField(max_length=50)
	email=models.EmailField(max_length=50)
	password=models.CharField(max_length=128)
	direccion=models.OneToOneField(Direcciones, on_delete=models.CASCADE, null=True, blank=True)
	rol=models.CharField(max_length=50)
	fecha_registro=models.DateField(auto_now_add=True)

