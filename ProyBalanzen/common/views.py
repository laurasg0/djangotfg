from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView # Import para las vistas y Para CBV
from django.views.generic import CreateView
from django.views.generic import UpdateView
from users.models import Usuario
from classes.models import SesionClase
from booking.models import Reserva

# VISTA DE PRUEBA (para crear formulario automatico)
# sin poner el template_name buscara user_form.html
class UserCreateView(CreateView):
    model = Usuario # Modelo asociado
    fields = ['nombre', 'email', 'password'] # Campos a mostrar en el formulario

# Vista de actualización de usuario
class UserUpdateView(UpdateView):
    model = Usuario
    fields = ['username', 'nombre', 'email', 'password']
    success_url = reverse_lazy('home')


# VISTAS BASADAS EN CLASES (CBV)
class HomeView(TemplateView):
    template_name = 'pages/home.html' # ruta a la plantilla

class LoginView(TemplateView):
    template_name ='pages/login.html' # ruta al login

class AdminView(TemplateView):
    template_name = 'pages/inicio_admin.html' # ruta a la plantilla del admin

    # función para pasar contexto adicional a la plantilla
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['total_usuarios'] = Usuario.objects.count()  
        context['clases_programadas'] = SesionClase.objects.count()
        context['reservas_totales'] = Reserva.objects.count()
        return context

class UserView(TemplateView):
    template_name = 'pages/inicio_user.html' # ruta a la plantilla del usuario

class ErrorView(TemplateView):
    template_name = 'pages/inicio_error.html' # ruta a la plantilla de error

