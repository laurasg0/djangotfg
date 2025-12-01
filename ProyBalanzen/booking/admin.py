from django.contrib import admin
from .models import Reserva

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'sesion', 'fecha_reserva', 'activa')
    list_filter = ('activa', 'fecha_reserva')
    search_fields = ('usuario__username', 'sesion__tipo_clase__nombre')
