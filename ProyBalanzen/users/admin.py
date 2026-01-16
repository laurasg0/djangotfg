from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(BaseUserAdmin):
    list_display = ('pk', 'email', 'nombre', 'apellidos', 'rol', 'nivel_membresia')  # Campos mostrados en la lista
    list_filter = ('rol', 'nivel_membresia')  # Filtros laterales
    search_fields = ('email', 'nombre', 'apellidos')  # Campos de búsqueda
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions')

    # Formulario para EDITAR usuarios existentes
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información adicional', {'fields': ('nombre', 'apellidos', 'telefono', 'fecha_nacimiento')}),
        ('Rol y membresía', {'fields': ('rol', 'puntos_recompensa', 'nivel_membresia')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login',)}),
    )

    # Formulario para CREAR nuevos usuarios
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),  # Incluye email en creación
        }),
        ('Información adicional', {
            'fields': ('nombre', 'apellidos', 'telefono', 'fecha_nacimiento')
        }),
        ('Rol y membresía', {
            'fields': ('rol', 'puntos_recompensa', 'nivel_membresia')
        }),
    )
