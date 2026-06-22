#!/usr/bin/env bash
# Salir inmediatamente si algún comando falla
set -o errexit

# Instalar dependencias
pip install -r requirements.txt

# Compilar archivos estáticos
python manage.py collectstatic --no-input

# Ejecutar migraciones de base de datos
python manage.py migrate
