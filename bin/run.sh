#!/bin/sh

if [[ "$1" == "production" ]]; then
    echo "starting server in production mode"
    su admin
    #statements
    DJANGO_SETTINGS_MODULE="sloth.settings_production" python3 manage.py runserver 0.0.0.0:8000 1>>log 2>&1 &
    celery -A sloth worker --loglevel=info 1>> celery.worker.log 2>&1 &
    celery -A sloth beat -l info 1>>celery.beat.log 2>&1
else
    echo "starting server in development mode"
    DJANGO_SETTINGS_MODULE="sloth.settings" python3 manage.py runserver 0.0.0.0:8000 1>>log 2>&1 &
    python manage.py celery -A sloth worker --loglevel=info &
    celery -A sloth beat -l info 1>>celery.beat.log 2>&1
fi
