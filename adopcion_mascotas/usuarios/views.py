#
# from django.contrib.auth import authenticate, login
# from .models import Usuario
#
# from django.shortcuts import render, redirect
# from django.contrib.auth.hashers import make_password
# from .forms import RegistroUsuarioForm
#
# def registrar_usuario(request):
#     if request.method == "POST":
#         usuario_form = RegistroUsuarioForm(request.POST)
#
#         if usuario_form.is_valid():
#             usuario = usuario_form.save(commit=False)
#             usuario.password = make_password(usuario.password)  # Encriptar contraseña
#
#             # Aquí no es necesario verificar el rol de refugio
#             if usuario.rol == "ADOPTANTE":
#                 usuario.save()  # Guarda el usuario adoptante
#
#                 # Redirige a login tras el registro exitoso
#                 return redirect("login")
#
#     else:
#         usuario_form = RegistroUsuarioForm()
#
#     return render(request, "usuarios/registro.html", {
#         "usuario_form": usuario_form,
#     })
#
#
# # def login_view(request):
# #     if request.method == "POST":
# #         email = request.POST["email"]
# #         password = request.POST["password"]
# #         usuario = Usuario.objects.filter(email=email).first()
# #
# #         if usuario and usuario.password == password:
# #             login(request, usuario)
# #             return redirect("home")  # Redirige a la página principal
# #
# #     return render(request, "usuarios/login.html")
#
# from django.contrib.auth import login
# from django.contrib.auth.hashers import check_password  # Importamos la función de verificación
# from django.shortcuts import render, redirect
# from .models import Usuario  # Asumiendo que 'Usuario' es tu modelo de usuario
#
#
# def login_view(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#
#         # Comprobamos si el usuario existe
#         usuario = Usuario.objects.filter(email=email).first()
#
#         if usuario and check_password(password, usuario.password):  # Comparamos la contraseña encriptada
#             login(request, usuario)  # Iniciar sesión
#             return redirect("home")  # Redirigir a la página principal
#
#         # Si la autenticación falla
#         error_message = "Email o contraseña incorrectos."
#         return render(request, "usuarios/login.html", {"error_message": error_message})
#
#     return render(request, "usuarios/login.html")
#
#
#
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from .forms import RegistroUsuarioForm
from .models import Usuario
from django.contrib.auth.hashers import make_password

def registrar_usuario(request):
    if request.method == "POST":
        usuario_form = RegistroUsuarioForm(request.POST)

        if usuario_form.is_valid():
            usuario = usuario_form.save(commit=False)
            usuario.password = make_password(usuario.password)  # Asegura que se guarde encriptada
            usuario.save()
            return redirect("login")

    else:
        usuario_form = RegistroUsuarioForm()

    return render(request, "usuarios/registro.html", {"usuario_form": usuario_form})



# def login_view(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#
#         usuario = Usuario.objects.filter(email=email).first()
#
#         if usuario and check_password(password, usuario.password):  # Verifica la contraseña encriptada
#             login(request, usuario)
#             return redirect("home")
#
#         error_message = "Email o contraseña incorrectos."
#         return render(request, "usuarios/login.html", {"error_message": error_message})
#
#     return render(request, "usuarios/login.html")


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

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