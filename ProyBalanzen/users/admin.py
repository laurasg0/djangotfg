from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Usuario, SesionUsuario

@admin.register(Usuario)
class UsuarioAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'nombre', 'apellidos', 'rol', 'nivel_membresia')  # Campos mostrados en la lista
    list_filter = ('rol', 'nivel_membresia', 'genero')  # Filtros laterales
    search_fields = ('username', 'email', 'nombre', 'apellidos')  # Campos de búsqueda
    
    # Formulario para EDITAR usuarios existentes
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Información adicional', {'fields': ('nombre', 'apellidos', 'telefono', 'fecha_nacimiento', 'genero')}),
        ('Rol y membresía', {'fields': ('rol', 'puntos_recompensa', 'nivel_membresia')}),
    )
    
    # Formulario para CREAR nuevos usuarios
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),  # Incluye email en creación
        }),
        ('Información adicional', {
            'fields': ('nombre', 'apellidos', 'telefono', 'fecha_nacimiento', 'genero')
        }),
        ('Rol y membresía', {
            'fields': ('rol', 'puntos_recompensa', 'nivel_membresia')
        }),
    )

@admin.register(SesionUsuario)
class SesionUsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'token_sesion', 'fecha_inicio', 'ultima_conexion', 'fecha_fin')  # Campos mostrados en la lista
    list_filter = ('fecha_inicio',)  # Filtros laterales
    search_fields = ('usuario__username', 'token_sesion')  # Búsqueda por usuario y token
    readonly_fields = ('fecha_inicio', 'ultima_conexion')  # Campos de solo lectura
