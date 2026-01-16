# Actividad 2:
a. entorno virtual --> .venv
b. proyecto: balanzen
c. superusuario creado
d. carpeta statics y media creadas y configuradas en settings.py
e. urls en balanzen
f. apps:
    - users: gestiona los usuarios (AbstractUser)
    - common: comunes a todo el proyecto (aquí están las views del proyecto)
    - classes:
    - centers
    - booking
    - ads
g. templates
h. docker compose up

# Actividad 3:
a. models de la base de datos implementados
b. función __str__ implementada
c. Meta en bookings (evita reservas duplicadas)

# Actividad 4:


# Levantar y migrar el proyecto
# Levanta los contenedores
docker-compose up -d

# Crea las migraciones EN ORDEN (de las que NO tienen dependencias a las que SÍ tienen)
docker-compose exec web python manage.py makemigrations users

docker-compose exec web python manage.py makemigrations centers

docker-compose exec web python manage.py makemigrations classes

docker-compose exec web python manage.py makemigrations booking

docker-compose exec web python manage.py makemigrations

docker-compose exec web python manage.py migrate

# recoger las static files
docker-compose exec web python manage.py collectstatic --noinput

# 6. Crea el superusuario
docker-compose exec web python manage.py createsuperuser