from django.shortcuts import render
from users.models import Usuario

# función que devuelve todos los usuarios
def get_users_all():
    usuarios = Usuario.objects.all()
    return usuarios

# función que devuelve un usuario por su ID
def get_user_by_id(user_id):
    try:
        usuario = Usuario.objects.get(id=user_id)
        return usuario
    except Usuario.DoesNotExist:
        return None

# función que crea un nuevo usuario
def create_user(username, email):
    nuevo_usuario = Usuario(username=username, email=email)
    nuevo_usuario.save()
    return nuevo_usuario

# función que actualiza un usuario existente
def update_user(user_id, username=None, email=None):
    try:
        usuario = Usuario.objects.get(id=user_id)
        if username:
            usuario.username = username
        if email:
            usuario.email = email
        usuario.save()
        return usuario
    except Usuario.DoesNotExist:
        return None
    
# función que elimina un usuario por su ID
def delete_user(user_id):
    try:
        usuario = Usuario.objects.get(id=user_id)
        usuario.delete()
        return True
    except Usuario.DoesNotExist:
        return False