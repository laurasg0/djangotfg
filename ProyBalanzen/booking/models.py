from django.db import models
from django.conf import settings
from classes.models import SesionClase

class Reserva(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reservas',
        verbose_name='Usuario'
    )
    sesion = models.ForeignKey(
        SesionClase,
        on_delete=models.CASCADE,
        related_name='reservas',
        verbose_name='Sesión'
    )
    fecha_reserva = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Reserva')
    activa = models.BooleanField(default=True, verbose_name='Activa')

    class Meta:
        unique_together = ('usuario', 'sesion')
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ['-fecha_reserva']  # Ordena por las reservas más recientes primero

    def __str__(self):
        return f"Reserva de {self.usuario.username} para {self.sesion}"