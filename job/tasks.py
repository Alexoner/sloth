from __future__ import absolute_import
from datetime import timedelta

from celery import shared_task
from celery.schedules import crontab


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

CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': timedelta(seconds=30),
        'args': (16, 16)
    },
}

#CELERY_TIMEZONE = 'UTC'

CELERYBEAT_SCHEDULE = {
    # Executes every Monday morning at 7:30 A.M
    'add-every-monday-morning': {
        'task': 'tasks.add',
        'schedule': crontab(hour='*', minute='*', day_of_week='*'),
        'args': (16, 16),
    },
}
