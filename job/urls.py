from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from job import views

urlpatterns = [
    url(r'^proxies/$', views.ProxyList.as_view()),
    url(r'^proxies/(?P<pk>[0-9]+)/$', views.ProxyDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
