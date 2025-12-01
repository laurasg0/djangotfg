from django.db import models

class Centro(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    direccion = models.CharField(max_length=255, verbose_name='Dirección')
    telefono = models.CharField(max_length=20, verbose_name='Teléfono')
    email = models.EmailField(verbose_name='Email')
    
    class Meta:
        verbose_name = 'Centro'
        verbose_name_plural = 'Centros'
        ordering = ['nombre']  # Ordena alfabéticamente por nombre
    
    def __str__(self):
        return self.nombre