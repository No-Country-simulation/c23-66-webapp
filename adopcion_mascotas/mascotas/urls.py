from .views import listar_mascotas
from django.urls import path

app_name = 'mascotas'
urlpatterns = [
   path('api/mascotas/', listar_mascotas, name='listar_mascotas') 
]
