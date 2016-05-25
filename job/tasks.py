from __future__ import absolute_import
from datetime import timedelta

from celery import shared_task
from celery.schedules import crontab
from celery.task.base import periodic_task
from django.core.mail import send_mail

@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def helloworld():
    print('hello world')
    return 'hello world'

@shared_task
@periodic_task(run_every=timedelta(days=10))
def email_sending_method():
    print('sending email')
    send_mail('subject', 'body', 'from_me@admin.com' ,
              ['to_him@gmail.com',], fail_silently=False)
