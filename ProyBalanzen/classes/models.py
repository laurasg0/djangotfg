from django.db import models
from django.utils.timezone import now

# Modelo de clases con nombre y descripción
class ClassType(models.Model):
    name = models.CharField(max_length=100, verbose_name='Clase')
    description = models.CharField(verbose_name='Descripción', null=False, blank=False)
    price = models.FloatField(verbose_name='Precio', null=False, blank=False)
    id_center = models.ForeignKey(
        'centers.Center',
        on_delete=models.CASCADE,
        related_name='Centro'
    )

    def __str__(self):
        return self.name
    
# Modelo ClassSession (solo define la sesión)
class ClassSession(models.Model):
    date = models.DateField(verbose_name="Fecha")
    start_time = models.TimeField(verbose_name="Hora de inicio")
    end_time = models.TimeField(verbose_name="Hora de fin")
    max_capacity = models.IntegerField(verbose_name='Capacidad')
    is_active = models.BooleanField(default=True, verbose_name="Sesión activa")

    class_type = models.ForeignKey(
        ClassType,
        on_delete=models.CASCADE,
        related_name='sessions'
    )

    def __str__(self):
        return f"{self.class_type.name} - {self.date} {self.start_time}"
