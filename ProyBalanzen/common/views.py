from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import TemplateView # Import para las vistas y Para CBV
from users.models import Usuario
from classes.models import SesionClase
from booking.models import Reserva

# VISTAS COMUNES A TODO EL PROYECTO


# VISTAS BASADAS EN CLASES (CBV)
class HomeView(TemplateView):
    template_name = 'pages/home.html' # ruta a la plantilla

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




