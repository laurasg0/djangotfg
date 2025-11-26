from django.db import models
from django.utils.timezone import now

# TODO: cambiar y extender de AbstractUser
class User(models.Model):

    class Gender(models.TextChoices):
        MUJER = 'MUJER', 'Mujer'
        HOMBRE = 'HOMBRE', 'Hombre'
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
    email = models.EmailField(max_length=300, verbose_name='Correo Electrónico', null=False, blank=False, unique=True)
    password = models.CharField(max_length=50, verbose_name='Contraseña', null=False, blank=False)
    phone = models.CharField(max_length=20, verbose_name='Teléfono', null=False, blank=False)
    birthdate = models.DateField(verbose_name= 'Fecha de Nacimiento', blank=True, null = True, default=None)
    gender = models.CharField(max_length=10, choices=Gender.choices, verbose_name='Género', default=None, null = True)
    role = models.CharField(max_length=10, choices=Role.choices, verbose_name='Rol', default=Role.CLIENTE)
    register_date = models.DateTimeField(verbose_name='Fecha de Registro', default=now, null=False, blank=False)
    reward_points = models.IntegerField(verbose_name='Balanzen Points', default=0, null=False, blank=False)
    membership_level = models.CharField(max_length=10, choices=Membership.choices, default=Membership.PLATA, null=False, blank=False)
    last_connection = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} {self.surname}"
    
# 1:M Un usuario puede tener una o más sesiones 

class UserSession(models.Model):
    token_session = models.CharField(max_length=255, unique=True)
    start_date = models.DateTimeField(default=now)
    end_date = models.DateTimeField(null=True, blank=True)
    id_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sessions'
    )

# crear app de session1