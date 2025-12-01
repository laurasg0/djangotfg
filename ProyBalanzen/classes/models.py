from django.db import models
from django.utils.timezone import now

# Modelo de clases con nombre y descripción
class TipoClase(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    descripcion = models.CharField(verbose_name='Descripción', null=False, blank=False)
    precio = models.FloatField(verbose_name='Precio', null=False, blank=False)
    centro = models.ForeignKey(
        'centers.Centro',
        on_delete=models.CASCADE,
        related_name='tipos_clase',
        verbose_name='Centro'
    )

    class Meta:
        verbose_name = 'Tipo de Clase'
        verbose_name_plural = 'Tipos de Clase'
        ordering = ['nombre']  # Ordena alfabéticamente

    def __str__(self):
        return self.nombre
    
# Modelo ClassSession (solo define la sesión)
class SesionClase(models.Model):
    fecha = models.DateField(verbose_name="Fecha")
    hora_inicio = models.TimeField(verbose_name="Hora de Inicio")
    hora_fin = models.TimeField(verbose_name="Hora de Fin")
    capacidad_maxima = models.IntegerField(verbose_name='Capacidad Máxima')
    activa = models.BooleanField(default=True, verbose_name="Sesión Activa")

    tipo_clase = models.ForeignKey(
        TipoClase,
        on_delete=models.CASCADE,
        related_name='sesiones',
        verbose_name='Tipo de Clase'
    )

    class Meta:
        verbose_name = 'Sesión de Clase'
        verbose_name_plural = 'Sesiones de Clase'
        ordering = ['-fecha', 'hora_inicio']  # Ordena por fecha descendente, luego por hora ascendente

    def __str__(self):
        return f"{self.tipo_clase.nombre} - {self.fecha} {self.hora_inicio}"
