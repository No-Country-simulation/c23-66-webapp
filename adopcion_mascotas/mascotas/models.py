from django.db import models

class Mascota(models.Model):
    id_mascota = models.AutoField(primary_key=True)
    nombre_mascota = models.CharField(max_length=50)
    edad_mascota = models.IntegerField(blank=True, null=True)
    especie = models.CharField(max_length=50, blank=True, null=True)
    raza = models.CharField(max_length=50, blank=True, null=True)
    tamaño = models.CharField(max_length=50, blank=True, null=True)
    descripcion_mascota = models.TextField(blank=True, null=True)
    foto = models.ImageField(blank=True, null=True)
    estado_salud = models.CharField(max_length=100, blank=True, null=True)
    id_refugio = models.IntegerField()
    fecha_registro = models.DateTimeField(blank=True, null=True)

    def str(self):
        return self.nombre_mascota
