from django.test import TestCase
from job.models import Proxy

# Create your tests here.

class TaskTestCase(TestCase):

    def setUp(self):
        pass

    def test_can_crawl_proxies(self):
        """ the task to crawl proxies functions well when scheduled by celery """
        print("can crawl proxies?")
        from job.tasks import crawl_proxies
        result = crawl_proxies.delay()
        assert result.successful()
        assert result.get() is True

    def test_foo(self):
        assert True

class ProxyTestCase(TestCase):

    def test_can_crud(self):
        address = 'http://username:password@127.0.0.1:8087/'
        proxy = Proxy(address=address)
        proxy.save()

        proxy = Proxy.objects.get(address=address)
        assert proxy.address == address

        source = 'test'
        proxy.source = source
        proxy.save()

        proxy = Proxy.objects.get(address=address)
        assert proxy.source == source

        proxy.delete()

        assert not Proxy.objects.filter(address=address).exists()
