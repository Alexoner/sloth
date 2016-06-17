#!/bin/sh

if [[ "$1" == "production" ]]; then
    #statements
    DJANGO_SETTINGS_MODULE="sloth.settings_production" su -m admin -c "python manage.py runserver 0.0.0.0:8000 1>>log 2>&1" &
    su -m admin -c "python manage.py celery -A sloth worker --loglevel=info" 1>> celery.worker.log 2>&1 &
    su -m admin -c "celery -A sloth beat -l info" 1>>celery.beat.log 2>&1
else
    DJANGO_SETTINGS_MODULE="sloth.settings" python manage.py runserver 0.0.0.0:8000 1>>log 2>&1 &
    python manage.py celery -A sloth worker --loglevel=info &
    celery -A sloth beat -l info 1>>celery.beat.log 2>&1
fi
