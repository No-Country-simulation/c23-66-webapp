from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

from refugios.models import Refugio
from .forms import RegistroUsuarioForm


def registrar_usuario(request):
	if request.method == "POST":
		usuario_form = RegistroUsuarioForm(request.POST)

		if usuario_form.is_valid():
			usuario = usuario_form.save(commit=False)  # No guardamos aún
			usuario.password = make_password(usuario.password)  # Encriptamos contraseña
			usuario.save()  # Ahora sí lo guardamos

			# Verificar el rol y crear el refugio si corresponde
			if usuario.rol == "REFUGIO":
				nombre_refugio = request.POST.get("nombre_refugio")  # Obtenerlo directamente del POST
				if nombre_refugio:  # Validar que haya nombre
					refugio = Refugio.objects.create(
						nombre=nombre_refugio,
						usuario=usuario,
						telefono="",  # Puedes cambiarlo
						descripcion="",
						direccion=None
					)
					refugio.save()

			return redirect("login")

	else:
		usuario_form = RegistroUsuarioForm()

	return render(request, "usuarios/registro.html", {"usuario_form": usuario_form})


def login_view(request):
	if request.method == "POST":
		email = request.POST.get("email")
		password = request.POST.get("password")

		user = authenticate(request, username=email, password=password)
		if user:
			login(request, user)
			return redirect("home")  # Asegúrate de que 'home' está en tus urls

		return render(request, "usuarios/login.html", {"error_message": "Credenciales incorrectas"})

	return render(request, "usuarios/login.html")


def logout_view(request):
	logout(request)
	return redirect('home')
