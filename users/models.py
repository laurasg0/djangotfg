from django.db import models
from django.utils.timezone import now

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre', null=False, blank=False)
    surname = models.CharField(max_length=150, verbose_name='Apellidos', null=False, blank=False)
    email = models.CharField(max_length=250, verbose_name='Correo Electrónico', null=False, blank=False)
    phone = models.IntegerField(max_length=9, verbose_name='Teléfono')
    password = models.CharField(max_length=50, verbose_name='Contraseña', null=False, blank=False)
    Rol = models.OneToOneField(Rol, verbose_name='Rol', related_name='roles')
    register_date = models.DateTimeField(verbose_name = 'Fecha de Registro', default=now)

class Rol(models.Model):
    name = models.CharField(max_length = 50, verbose_name = 'Name')


# campo DateTimeField para guardar la última conexión

# crear app de session