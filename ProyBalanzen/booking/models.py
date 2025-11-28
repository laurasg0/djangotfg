from django.db import models
from django.conf import settings    # Importa la configuración del proyecto para usar el modelo de usuario
from classes.models import ClassSession

class Booking(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,   # Referencia al modelo de usuario en settings.py
        on_delete=models.CASCADE,
        related_name='Reservas')
    session = models.ForeignKey(
        ClassSession,
        on_delete = models.CASCADE,
        related_name = 'Reservas')
    booked_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('user', 'session') # Evita reservas duplicadas

    def __str__(self):
        return f"Reserva de {self.user.username} para {self.session}"