from __future__ import unicode_literals

from django.db import models

# Create your models here.
class GitHubHookConf(models.Model):

    # owner = models.ForeignKey('auth.User', related_name='proxies', default=1)

    created      = models.DateTimeField(auto_now_add=True)
    name         = models.CharField(max_length=32, blank=False)
    url          = models.CharField(max_length=255, blank=False, default='')
    # comma separated paths: path1,path2,...,pathN
    paths         = models.CharField(max_length=100, blank=True)
    # the install scripts
    install = models.TextField(blank=True)

    class Meta:
        ordering = ('name', '-created')

    def save(self, *args, **kwargs):
        """
        """
        super(GitHubHookConf, self).save(*args, **kwargs)

