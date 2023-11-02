#!/bin/sh

python3 manage.py makemigrations

python3 manage.py migrate

if [ ! -f /app/static/.last_modified ]; then
    python3 manage.py collectstatic
    touch /app/static/.last_modified
fi

python3 manage.py test

gunicorn mindtify.wsgi:application --bind 0.0.0.0:8000