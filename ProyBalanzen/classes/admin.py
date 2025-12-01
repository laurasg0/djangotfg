from django.contrib import admin
from .models import TipoClase, SesionClase

@admin.register(TipoClase)
class TipoClaseAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'centro')
    search_fields = ('nombre',)
    list_filter = ('centro',)

@admin.register(SesionClase)
class SesionClaseAdmin(admin.ModelAdmin):
    list_display = ('tipo_clase', 'fecha', 'hora_inicio', 'hora_fin', 'capacidad_maxima', 'activa')
    list_filter = ('activa', 'fecha', 'tipo_clase')
    search_fields = ('tipo_clase__nombre',)
