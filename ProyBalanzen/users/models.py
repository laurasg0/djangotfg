from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class Usuario(AbstractUser):

    class Genero(models.TextChoices):
        MUJER = 'MUJER', 'Mujer'
        HOMBRE = 'HOMBRE', 'Hombre'
        OTRO = 'OTRO', 'Otro'

    class Rol(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        TRABAJADOR = 'TRABAJADOR', 'Trabajador'
        CLIENTE = 'CLIENTE', 'Cliente'

    class Membresia(models.TextChoices):
        PLATA = 'PLATA', 'Plata'
        ORO = 'ORO', 'Oro'
        PLATINO = 'PLATINO', 'Platino'

    # Campos adicionales
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellidos = models.CharField(max_length=150, verbose_name='Apellidos')
    telefono = models.CharField(max_length=20, verbose_name='Teléfono')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de Nacimiento', blank=True, null=True)
    genero = models.CharField(max_length=10, choices=Genero.choices, default=None, null=True)
    rol = models.CharField(max_length=15, choices=Rol.choices, default=Rol.CLIENTE)
    puntos_recompensa = models.IntegerField(default=0, verbose_name='Puntos de Recompensa')
    nivel_membresia = models.CharField(max_length=10, choices=Membresia.choices, default=Membresia.PLATA, verbose_name='Nivel de Membresía')

    # Modificación del email
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['username']  # Ordena alfabéticamente por nombre de usuario

    def __str__(self):
        return f"{self.username} - {self.email}" # Mostrar nombre de usuario y email


class SesionUsuario(models.Model):
    token_sesion = models.CharField(max_length=255, unique=True, verbose_name='Token de Sesión')
    fecha_inicio = models.DateTimeField(default=timezone.now, verbose_name='Fecha de Inicio')
    fecha_fin = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de Fin')
    ultima_conexion = models.DateTimeField(null=True, blank=True, verbose_name='Última Conexión')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='sesiones')

    # clase meta para definir nombres en singular y plural
    class Meta:
        verbose_name = 'Sesión de Usuario'
        verbose_name_plural = 'Sesiones de Usuario'
        ordering = ['-fecha_inicio']  # Ordena por fecha más reciente primero (el - indica descendente)

    # Método para actualizar la última conexión
    def actualizar_conexion(self):
        self.ultima_conexion = timezone.now()
        self.save(update_fields=['ultima_conexion'])

    # Método string para representar la sesión
    def __str__(self):
        return f"Sesión {self.pk} de {self.usuario.email}"
