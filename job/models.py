from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Proxy(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    url     = models.CharField(max_length=100, blank=False, default='')
    source  = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=16, blank=True)
    type    = models.CharField(max_length=16, blank=True)

    class Meta:
        ordering = ('-created',)
