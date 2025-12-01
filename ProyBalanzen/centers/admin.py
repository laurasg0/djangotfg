from django.contrib import admin
from .models import Centro

@admin.register(Centro)
class CentroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono', 'email')  # Campos que se muestran en la lista del admin
    search_fields = ('nombre', 'direccion')  # Campos por los que se puede buscar
