"""
URL configuration for balanzen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from common import views as common_views # Importamos las vistas de common
from users import views as users_views # Importamos las vistas de users

urlpatterns = [
    path('admin/', admin.site.urls),
    # añadir siempre el nombre para poder llamarlo
    path('', common_views.HomeView.as_view(), name='home'), # VISTA PRINCIPAL AL ABRIR LA PÁGINA (view en common)
    path('signup/', users_views.SignupView.as_view(), name='signup'),
    path('login/', users_views.LoginFormView.as_view(), name='login'),
    path('logout/', users_views.LogoutFormView.as_view(), name='logout'), 
    path('inicio_admin/', common_views.AdminView.as_view(), name='inicio_admin'),
    path('inicio_user/', common_views.UserView.as_view(), name='inicio_user'),
    path('inicio_error/', common_views.ErrorView.as_view(), name='inicio_error'),
    path('create/', users_views.UserCreateView.as_view(), name='crear'),
    path('update/<int:pk>/', users_views.UserUpdateView.as_view(), name='editar'), # Vista de formulario de usuario
    path('delete/<int:pk>/', users_views.UserDeleteView.as_view(), name='eliminar'), # Vista para eliminar usuario
    path('paginacion/', users_views.paginacion_view, name='paginacion'),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
