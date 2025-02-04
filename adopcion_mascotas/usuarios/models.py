from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from direcciones.models import Direccion


# Manager personalizado para manejar usuarios
class UsuarioManager(BaseUserManager):
	def create_user(self, email, nombre, password=None, **extra_fields):
		if not email:
			raise ValueError("El usuario debe tener un email válido")

		email = self.normalize_email(email)
		usuario = self.model(email=email, nombre=nombre, **extra_fields)
		usuario.set_password(password)  # Encripta la contraseña
		usuario.save(using=self._db)
		return usuario

	def create_superuser(self, email, nombre, password=None, **extra_fields):
		extra_fields.setdefault("is_staff", True)
		extra_fields.setdefault("is_superuser", True)
		return self.create_user(email, nombre, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):  # Hereda de AbstractBaseUser
	ROLES = [
		("ADOPTANTE", "Adoptante"),
		("REFUGIO", "Refugio"),
	]

	email = models.EmailField(unique=True)
	nombre = models.CharField(max_length=50)
	direccion = models.OneToOneField(Direccion, on_delete=models.CASCADE, null=True, blank=True)
	rol = models.CharField(max_length=50, choices=ROLES)
	fecha_registro = models.DateField(auto_now_add=True)

	# Campos requeridos para autenticación en Django
	is_active = models.BooleanField(default=True)  # Necesario para autenticación
	is_staff = models.BooleanField(default=False)  # Necesario para administración

	objects = UsuarioManager()  # Usamos nuestro propio manager

	USERNAME_FIELD = "email"  # El campo que se usará para loguearse
	REQUIRED_FIELDS = ["nombre"]  # Campos requeridos al crear un superusuario

	def __str__(self):
		return self.email
