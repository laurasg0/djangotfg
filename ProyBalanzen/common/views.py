from django.shortcuts import render
from django.views.generic import TemplateView # Import para las vistas y Para CBV

# Create your views here.
class HomeView(TemplateView):
    template_name = 'pages/home.html' # ruta a la plantilla

class LoginView(TemplateView):
    template_name ='pages/login.html' # ruta al login

class AdminView(TemplateView):
    template_name = 'pages/inicio_admin.html' # ruta a la plantilla del admin

class UserView(TemplateView):
    template_name = 'pages/inicio_user.html' # ruta a la plantilla del usuario

class ErrorView(TemplateView):
    template_name = 'pages/inicio_error.html' # ruta a la plantilla de error