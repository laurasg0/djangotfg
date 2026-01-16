from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import TemplateView # Import para las vistas y Para CBV
from users.models import Usuario

# VISTAS BASADAS EN CLASES (CBV) RELACIONADAS CON USUARIOS

# FORMULARIOS AUTOMÁTICOS
# sin poner el template_name buscara user_form.html
class UserCreateView(CreateView):
    model = Usuario # Modelo asociado
    fields = ['nombre', 'apellidos', 'email', 'password', 'telefono', 'fecha_nacimiento'] # Campos a mostrar en el formulario
    success_url = reverse_lazy('home') # URL de redirección tras el éxito
    def form_valid(self, form):
        usuario = form.save(commit=False)
        usuario.set_password(form.cleaned_data['password'])  # Hashear la contraseña
        usuario.save()
        return super().form_valid(form)
    # sobreescribimos el metodo para mandar más datos guardados en context y lo devolvemos
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear un nuevo usuario'
        return context

# Actualización de usuario
class UserUpdateView(UpdateView):
    model = Usuario
    fields = ['nombre', 'apellidos', 'email', 'password', 'telefono', 'fecha_nacimiento']
    
    def form_valid(self, form):
        usuario = form.save(commit=False)
        usuario.set_password(form.cleaned_data['password'])  # Hashear la contraseña
        usuario.save()
        return super().form_valid(form)
    success_url = reverse_lazy('paginacion') # Redirigir a la vista de paginación tras actualizar

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar usuario'
        return context

# Eliminación de usuario
class UserDeleteView(DeleteView):
    model = Usuario
    success_url = reverse_lazy('paginacion') # Redirigir a la vista de paginación tras eliminar

# LOGIN Y LOGOUT
class LoginFormView(LoginView):
    template_name = 'pages/login.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesión'
        return context
    
    # Redirigir según el rol del usuario
    def get_success_url(self):
        user = self.request.user
        if user.rol == 'ADMIN' or user.rol == 'TRABAJADOR':
            return reverse_lazy('inicio_admin')
        else:
            return reverse_lazy('inicio_user')

class LogoutFormView(LogoutView):
    success_url = reverse_lazy('home')
    http_method_names = ['get', 'post', 'options']

# PAGINACIÓN
# Función para la paginación
def paginacion_view(request):
    usuarios_list = Usuario.objects.all()
    paginator = Paginator(usuarios_list, 10)  # Mostrar 10 usuarios por página

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pages/prueba_paginacion.html', {'page_obj': page_obj})

class PaginacionView(TemplateView):
    template_name = 'pages/prueba_paginacion.html' # PROBANDO PAGINACIÓN


class SignupView(TemplateView):
    template_name = 'pages/signup.html' # ruta al registro de usuarios