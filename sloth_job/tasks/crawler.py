from __future__ import absolute_import
from datetime import timedelta
from logging import log, DEBUG, INFO
import time

from celery import shared_task
from celery.schedules import crontab
from celery.task.base import periodic_task
from scrapyd_api import ScrapydAPI

DEFAULT_URL = 'http://localhost:6800/'

@shared_task
def start_dbworker():
    # TODO: run the spider worker
    # laod seeds from db
    # pid lock
    pass

@shared_task
def schedule_job(project,
                 spider,
                 url=DEFAULT_URL,
                 settings={}, **kwargs):
    """
    @param project: scrapy project name
    @param spider: spider name
    @param url: the url which target scrapyd daemon listens on
    @param settings: the settings dictionary

    To schedule a spider run:
        curl http://localhost:6800/schedule.json -d project=myproject -d spider=spider2
    """
    scrapyd = ScrapydAPI(url)
    return scrapyd.schedule(project, spider, settings, **kwargs)

@shared_task
def cancel_job(project,
               spider,
               url=DEFAULT_URL):
    """
    @param project: scrapy project name
    @param spider: spider name
    @param url: the url which target scrapyd daemon listens on
    @param settings: the settings dictionary

    To schedule a spider run:
        curl http://localhost:6800/schedule.json -d project=myproject -d spider=spider2
    """
    scrapyd = ScrapydAPI(url)
    return scrapyd.cancel(project, spider)

@shared_task
def list_jobs(project,
              url=DEFAULT_URL):
    """
    @param project: scrapy project name
    @param spider: spider name
    @param url: the url which target scrapyd daemon listens on
    @param settings: the settings dictionary

    To schedule a spider run:
        curl http://localhost:6800/schedule.json -d project=myproject -d spider=spider2
    """
    scrapyd = ScrapydAPI(url)
    return scrapyd.list_jobs(project)
    pass

@shared_task
def job_status(project, job, url=DEFAULT_URL):
    scrapyd = ScrapydAPI(url)
    return scrapyd.job_status(project, job)

@shared_task
def delete_project(project, url=DEFAULT_URL):
    """
    @param project: scrapy project name
    @param spider: spider name
    @param url: the url which target scrapyd daemon listens on
    @param settings: the settings dictionary

    To schedule a spider run:
        curl http://localhost:6800/schedule.json -d project=myproject -d spider=spider2
    """
    scrapyd = ScrapydAPI(url)
    return scrapyd.delete_project(project)

@shared_task
def delete_version(project, version, url=DEFAULT_URL):
    scrapyd = ScrapydAPI(url)
    return scrapyd.delete_version(project, version)
