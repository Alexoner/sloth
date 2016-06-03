from __future__ import unicode_literals

from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

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
        # lexer = get_lexer_by_name(self.language)
        # linenos = self.linenos and 'table' or False
        # options = self.title and {'title': self.title} or {}
        # formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  # full=True, **options)
        # self.highlighted = highlight(self.address, formatter)
        super(Proxy, self).save(*args, **kwargs)
