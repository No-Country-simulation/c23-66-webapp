from django.db import models
from usuarios.models import Usuario
# Create your models here.
class Adopciones(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    # id_mascota = models.ForeignKey(Mascota, on_delete= models.CASCADE)
    estado = models.CharField(max_length=20)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_aprobacion = models.DateTimeField()
    comentarios = models.CharField(max_length=500)