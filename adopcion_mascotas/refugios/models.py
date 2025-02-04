from django.db import models

from direcciones.models import Direccion
from usuarios.models import Usuario


# Create your models here.
class Refugio(models.Model):
	nombre = models.CharField(max_length=100)
	direccion = models.OneToOneField(Direccion, on_delete=models.CASCADE, related_name="refugios")
	usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name="refugios")
	telefono = models.CharField(max_length=100)
	descripcion = models.TextField()

	def __str__(self):
		return self.nombre