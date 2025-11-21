from django.db import models
from django.utils.timezone import now

# Create your models here.
class Users(models.Model):

    class Gender(models.TextChoices):
        MUJER = 'MUJER', 'Mujer'
        HOMBRE = 'Hombre', 'Hombre'
        OTRO = 'OTRO', 'Otro'
    
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        TRABAJADOR = 'TRABAJADOR', 'Trabajador'
        CLIENTE = 'CLIENTE', 'Cliente'

    class Membership(models.TextChoices):
        PLATA = 'PLATA', 'Plata'
        ORO = 'ORO', 'Oro'
        PLATINO = 'PLATINO', 'Platino'
        
    
    name = models.CharField(max_length=50, verbose_name='Nombre', null=False, blank=False)
    surname = models.CharField(max_length=150, verbose_name='Apellidos', null=False, blank=False)
    email = models.EmailField(max_length=250, verbose_name='Correo Electrónico', null=False, blank=False)
    password = models.CharField(max_length=50, verbose_name='Contraseña', null=False, blank=False)
    phone = models.CharField(verbose_name='Teléfono')
    birthdate = models.DateTimeField(verbose_name= 'Fecha de Nacimiento', blank=True, default=None)
    gender = models.CharField(max_length=10, choices=Gender.choices, verbose_name='Género', default=None)
    role = models.CharField(max_length=10, choices=Role.choices, verbose_name='Rol', default=Role.CLIENTE)
    register_date = models.DateTimeField(verbose_name='Fecha de Registro', default=now)
    reward_points = models.IntegerField(verbose_name='Balanzen Points', default=0)
    membership_level = models.CharField(max_length=10, choices=Membership.choices, default=Membership.PLATA)
    
    def __str__(self):
        return f"{self.name} {self.surname}"
    
class Session(models.Model):
    token_session = models.CharField(max_length=255, unique=True)
    start_date = models.DateTimeField(default=now)
    end_date = models.DateTimeField(null=True, blank=True)


# campo DateTimeField para guardar la última conexión

# crear app de session1