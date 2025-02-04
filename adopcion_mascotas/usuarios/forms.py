from django import forms

from .models import Usuario


class RegistroUsuarioForm(forms.ModelForm):
	nombre_refugio = forms.CharField(max_length=100, required=False)  # Campo adicional para refugio

	class Meta:
		model = Usuario
		fields = ['email', 'nombre', 'password', 'rol']

	rol = forms.ChoiceField(
		choices=[("ADOPTANTE", "adoptante"), ("REFUGIO", "refugio")],
		widget=forms.RadioSelect,
		required=True
	)

	def save(self, commit=True):
		usuario = super().save(commit=False)  # NO se guarda aquí
		return usuario  # Devolvemos el usuario sin guardar
