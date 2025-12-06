# Para generar datos simulados
from faker import Faker
from users.models import Usuario
import random

fake = Faker("es_ES") # para poner ñ jaja

def crear_usuarios(n):
    for _ in range(n):
        Usuario.objects.create(
            username = fake.unique.user_name()[:20], # limitar a 20 caracteres
            nombre = fake.name(),
            apellidos = fake.last_name(),
            telefono = fake.phone_number(),
            fecha_nacimiento = fake.date_of_birth(minimum_age=16, maximum_age=80),
            genero = random.choice([choice[0] for choice in Usuario.Genero.choices]),
            puntos_recompensa = random.randint(0, 1000),
            nivel_membresia = random.choice([choice[0] for choice in Usuario.Membresia.choices]),
            email = fake.unique.email(),
        )