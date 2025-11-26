from django.db import models
from django.utils.timezone import now

# Modelo de clases con nombre y descripción
class Classes(models.Model):
    name = models.CharField(max_length=50, verbose_name='Clase', null=False, blank=False)
    description = models.CharField(max_length=150, verbose_name='Descripción', null=False, blank=False)
    price = models.FloatField(verbose_name='Precio', null=False, blank=False)
    # TODO: ID_CENTER FK

    def __str__(self):
        return self.name
    
# Modelo Turn (Reserva de clase por usuario)
class Turn(models.Model):
    date = models.DateField(verbose_name='Fecha', null=False, blank=False)
    time = models.TimeField(verbose_name='Hora', null=False, blank=False)
    capacity = models.IntegerField(verbose_name='Capacidad', null=False, blank=False)
    id_user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='turns'
    )
    id_class = models.ForeignKey(
        Classes,
        on_delete=models.CASCADE,
        related_name='turns'
    )