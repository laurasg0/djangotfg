from django.shortcuts import render
from django.views.generic import TemplateView # Import para las vistas y Para CBV

# Create your views here.
class HomeView(TemplateView):
    template_name = 'pages/home.html' # ruta a la plantilla
