from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):

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

    # Campos adicionales
    name = models.CharField(max_length=50, verbose_name='Nombre')
    surname = models.CharField(max_length=150, verbose_name='Apellidos')
    phone = models.CharField(max_length=20, verbose_name='Teléfono')
    birthdate = models.DateField(verbose_name='Fecha de Nacimiento', blank=True, null=True)
    gender = models.CharField(max_length=10, choices=Gender.choices, default=None, null=True)
    role = models.CharField(max_length=15, choices=Role.choices, default=Role.CLIENTE)
    reward_points = models.IntegerField(default=0)
    membership_level = models.CharField(max_length=10, choices=Membership.choices, default=Membership.PLATA)

    # Modificación del email
    email = models.EmailField(unique=True)

    # El AbstractUser ya trae: password hasheado, username, is_staff, etc.

    def __str__(self):
        return f"{self.username} - {self.email}"


class UserSession(models.Model):
    token_session = models.CharField(max_length=255, unique=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True, blank=True)
    last_connection = models.DateTimeField(null=True, blank=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sessions')

    def touch(self):
        self.last_connection = timezone.now()
        self.save(update_fields=['last_connection'])

    def __str__(self):
        return f"Session {self.pk} for {self.user.email}"
