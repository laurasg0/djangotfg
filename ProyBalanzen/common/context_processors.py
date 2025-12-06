from django.contrib.auth import get_user_model

# Usa context_processors si:

# El dato debe estar disponible en todas las plantillas.

# Es algo global, por ejemplo:

# Nombre del sitio

# Configuraciones globales

# Datos que aparecen en el header o footer

# La consulta es muy ligera (ej. solo leer una constante).

# Desventaja

# Se ejecuta en cada petición que renderiza una plantilla.

# Para datos que cambian o requieren consulta a BD, puede costar más.
