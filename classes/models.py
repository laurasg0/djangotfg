from django.db import models
from django.utils.timezone import now

# Modelo de clases con nombre y descripción
class Classes(models.Model):
    name = models.CharField(max_length=50, verbose_name='Clase', null=False, blank=False)
    description = models.CharField(max_length=150, verbose_name='Descripción', null=False, blank=False)
    price = models.FloatField(verbose_name='Precio', null=False, blank=False)