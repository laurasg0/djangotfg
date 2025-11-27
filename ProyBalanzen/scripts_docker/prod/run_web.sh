#!/bin/sh
exec su -m django_user -c "gunicorn --chdir /code/ProyBalanzen --bind 0.0.0.0:8000 
ProyBalanzen.wsgi:application"
# TODO: MODIFICAR PORQUE NO VA
