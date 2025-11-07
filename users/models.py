from django.db import models
from django.utils.timezone import now

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name', null=False, blank=False)
    surname = models.CharField(max_length=150, verbose_name='Surname', null=False, blank=False)
    email = models.CharField()
    phone = models.IntegerField(max_length=9, verbose_name='Phone')
    password = models.CharField(max_length=50, verbose_name='Password', null=False, blank=False)
    Rol = models.OneToOneField(Rol, verbose_name='Rol', related_name='roles')
    register_date = models.DateTimeField(verbose_name = 'Register date', default=now)

class Rol(models.Model):
    name = models.VharFIeld(max_length = 50, verbose_name = 'Name')