from django.conf.urls import url
from job import views

urlpatterns = [
    url(r'^proxies/$', views.proxy_list),
    url(r'^proxies/(?P<pk>[0-9]+)/$', views.proxy_detail),
]
