from django.db import models

# Create your models here.
class Direcciones(models.Model):
	calle =models.CharField(max_length=100)
	numero =models.CharField(max_length=10)
	ciudad = models.CharField(max_length=50)
	estado = models.CharField(max_length=50)
	pais = models.CharField(max_length=50)
	codigo_postal = models.CharField(max_length=20)
	fecha_creacion = models.DateTimeField(auto_now=True)
	fecha_modificacion = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.calle} {self.numero} {self.ciudad} {self.estado} {self.pais.name} {self.codigo_postal} {self.fecha_creacion} {self.fecha_modificacion}"
