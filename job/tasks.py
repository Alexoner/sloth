from __future__ import absolute_import
from datetime import timedelta
import time

from celery import shared_task
from celery.schedules import crontab
from celery.task.base import periodic_task
from django.core.mail import send_mail
from logging import log, DEBUG, INFO

from job.models import Proxy

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
def run_crawler(spider_name='general',
                origin='https://github.com/Alexoner/web-crawlers.git',
                seeds=None):
    # TODO: initialize local env
    # 1. mkdir
    # 2. checkout out latest source code from origin
    # 3. virtualenv && pip install -r requirements.txt

    if not 'init env succeeded':
        return {
            'status_code': 500,
            'msg': 'pip install is taking too long',
        }

    # TODO: run the spider worker
    # laod seeds from db
    # pid lock

    # TODO: dispatch the crawler workers
    # through scrapyd daemon API or
    # with batch shell scripts
    pass


import asyncio
from proxybroker import Broker

@shared_task
def crawl_proxies(limit=1000, countries=['CN']):

    async def save(proxies_crawled):
        """Save proxies to a file."""
        while True:
            log(INFO, 'awaiting for crawled proxy')
            proxy_crawled = await proxies_crawled.get()
            if proxy_crawled is None:
                log(DEBUG, 'got None for proxy_crawled, task finished')
                break
            log(INFO, proxy_crawled)
            proto = 'https' if 'HTTPS' in proxy_crawled.types else 'http'
            row = Proxy(
                address='%s://%s:%d\n' %
                (proto, proxy_crawled.host, proxy_crawled.port))
            log(DEBUG,  row.address )
            row.save()

    def main():
        proxies = asyncio.Queue()
        broker = Broker(proxies)
        tasks = asyncio.gather(broker.find(types=['HTTP', 'HTTPS'], countries=countries, limit=limit),
                               save(proxies))

        loop = asyncio.new_event_loop()
        try:
            # FIXME: raises OSError: [Errno 9] Bad file descriptor
            loop.run_until_complete(tasks)
        except OSError as e:
            print('tasked failed', 'loop:', loop, 'error:', e)
            return False
        finally:
            loop.close()

        return True

    return main()
