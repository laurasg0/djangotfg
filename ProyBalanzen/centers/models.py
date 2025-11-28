from django.db import models

class Center(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre del Centro', null=False, blank=False)
    address = models.CharField(max_length=255, verbose_name='Dirección', null=False, blank=False)
    city = models.CharField(max_length=100, verbose_name='Ciudad', null=False, blank=False)
    phone = models.CharField(max_length=20, verbose_name='Teléfono', null=False, blank=False)
    email = models.EmailField(verbose_name='Correo Electrónico', null=False, blank=False)
    opening_time = models.TimeField(verbose_name="Hora de apertura", null=True, blank=True)
    closing_time = models.TimeField(verbose_name="Hora de cierre", null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name="Centro activo")
    
    def __str__(self):
        return self.name