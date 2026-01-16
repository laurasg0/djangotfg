from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class UsuarioManager(BaseUserManager):
    # función para crear usuario normal
    def create_user(
            self, email, nombre, apellidos, password = None, telefono = None, fecha_nacimiento = None
    ):
        # crear y guardar un usuario con el email y la contraseña
        if not email:
            raise ValueError("Ha de proporcionar un e-mail válido")
        
        user = self.model(
            email = self.normalize_email(email),
            nombre = nombre,
            apellidos = apellidos,
            telefono = telefono,
            fecha_nacimiento = fecha_nacimiento,
        )

        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # función para crear un superusuario
    def create_superuser(self, email, password):
        if not email:
            raise ValueError("Ha de proporcionar un e-mail válido,")
        
        user = self.model(email=self.normalize_email(email))

        user.set_password(password)
        user.is_staff= True
        user.is_active = True
        user.is_superuser= True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser, PermissionsMixin):

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
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellidos = models.CharField(max_length=150, verbose_name='Apellidos')
    telefono = models.CharField(max_length=20, verbose_name='Teléfono')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de Nacimiento', blank=True, null=True)
    rol = models.CharField(max_length=15, choices=Rol.choices, default=Rol.CLIENTE)
    puntos_recompensa = models.IntegerField(default=0, verbose_name='Puntos de Recompensa')
    nivel_membresia = models.CharField(max_length=10, choices=Membresia.choices, default=Membresia.PLATA, verbose_name='Nivel de Membresía')
    activo = models.BooleanField(null=True, verbose_name='activo')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='fecha_creacion')
    update_date = models.DateTimeField(auto_now=True, verbose_name='fecha_actualizacion')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    # EMAIL COMO USUARIO
    USERNAME_FIELD = 'email'

    objects = UsuarioManager() # manager personalizado para crear usuarios

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['email']  # Ordena alfabéticamente por email

    def __str__(self):
        return f"{self.email}" # Mostrar email

