#!/bin/sh

DJANGO_SETTINGS_MODULE="sloth.settings" python manage.py runserver 0.0.0.0:8000 1>>log 2>&1
