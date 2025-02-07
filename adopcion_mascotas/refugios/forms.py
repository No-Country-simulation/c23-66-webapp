from django import forms
from .models import Refugio

class RegistroRefugioForm(forms.ModelForm):
    class Meta:
        model = Refugio
        fields = ["direccion", "telefono", "descripcion"]
