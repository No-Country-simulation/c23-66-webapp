from django.db import models
from seguimientos_adopciones.models import Adopciones
# Create your models here.
class seguimiento_adopciones(models.Model):
    id_adopcion = models.ForeignKey(Adopciones, on_delete=models.CASCADE)
    fecha_seguimiento = models.DateTimeField()
    estado_mascota = models.CharField(max_length=20)
    comentarios = models.CharField(max_length=500)