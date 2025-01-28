from django.http import JsonResponse
from .models import Mascota

def listar_mascotas(request):
    Mascotas = Mascotas.info('id_mascota', 'nombre_mascota', 'edad_mascota', 'especie', 'raza', 
'tamaño', 'descripcion_mascota', 'estado_salud', 'foto', 'id_refugio', 'fecha_registro')
    return JsonResponse(list(Mascotas), safe=False)
