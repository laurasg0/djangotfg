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
from common import views # Importamos las vistas de common

urlpatterns = [
    path('admin/', admin.site.urls),
    # añadir siempre el nombre para poder llamarlo
    path('', views.HomeView.as_view(), name='home'), # VISTA PRINCIPAL AL ABRIR LA PÁGINA (view en common)
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), # TODO: REVISAR auth_views!
    path('inicio_admin/', views.AdminView.as_view(), name='inicio_admin'),
    path('inicio_user/', views.UserView.as_view(), name='inicio_user'),
    path('inicio_error/', views.ErrorView.as_view(), name='inicio_error'),
    path('create/', views.UserCreateView.as_view(), name='crear'),
    path('update/<int:pk>/', views.UserUpdateView.as_view(), name='editar'), # Vista de formulario de usuario
    path('paginacion/', views.paginacion_view, name='paginacion')
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
