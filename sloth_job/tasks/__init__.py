from __future__ import absolute_import
from datetime import timedelta
from logging import log, DEBUG, INFO
import time

from celery import shared_task
from celery.schedules import crontab
from celery.task.base import periodic_task
from django.core.mail import send_mail

from .crawler import *

@shared_task
def add(x, y):
    return x + y

@shared_task
def helloworld():
    print('hello world')
    return 'hello world'

@shared_task
@periodic_task(run_every=timedelta(days=10))
def email_sending_method():
    print('sending email')
    send_mail('subject', 'body', 'from_me@admin.com',
              ['to_him@gmail.com', ], fail_silently=False)
    return True

@shared_task
def init_env():
    # TODO: initialize local env
    # 1. mkdir
    # 2. checkout out latest source code from origin
    # 3. virtualenv && pip install -r requirements.txt
    if not 'init env succeeded':
        return {
            'status_code': 500,
            'msg': 'pip install is taking way too long',
        }
    pass
