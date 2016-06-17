from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Proxy(models.Model):

    owner = models.ForeignKey('auth.User', related_name='proxies', default=1)

    created = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=100, blank=False, default='')
    source  = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=16, blank=True)
    type    = models.CharField(max_length=16, blank=True)

    class Meta:
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        super(Proxy, self).save(*args, **kwargs)
