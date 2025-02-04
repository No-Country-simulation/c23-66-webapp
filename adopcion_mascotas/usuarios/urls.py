
from django.urls import path
from .views import registrar_usuario,login_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("registro/", registrar_usuario, name="registro"),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('accounts/login/', login_view, name='login'),  # Login

]
