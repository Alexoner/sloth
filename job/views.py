from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from job.models import Proxy
from job.serializers import ProxySerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

# Create your views here.

@csrf_exempt
def proxy_list(request):
    """
    List all proxies, or create a new proxy.
    """
    if request.method == 'GET':
        proxies = Proxy.objects.all()
        serializer = ProxySerializer(proxies, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProxySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def proxy_detail(request, pk):
    """
    Retrieve, update or delete a code proxy.
    """
    try:
        proxy = Proxy.objects.get(pk=pk)
    except Proxy.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProxySerializer(proxy)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProxySerializer(proxy, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        proxy.delete()
        return HttpResponse(status=204)
