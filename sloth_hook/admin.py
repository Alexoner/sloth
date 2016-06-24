from django.contrib import admin

from .models import GitHubHookConf

# Register your models here.
@admin.register(GitHubHookConf)
class GitHubHookConfAdmin(admin.ModelAdmin):
    fields = ('name', 'url', 'paths', 'install')
