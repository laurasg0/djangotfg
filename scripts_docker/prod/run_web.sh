#!/bin/sh
cd /code
exec gunicorn --workers 3 --bind 0.0.0.0:8000 ProyBalanzen.wsgi:application