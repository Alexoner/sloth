#!/bin/sh

DJANGO_SETTINGS_MODULE="sloth.settings" python2 manage.py runserver 1>log 2>&1
