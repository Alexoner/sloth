from rest_framework import status
from rest_framework.views import APIView
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from job.models import Proxy
from job.serializers import ProxySerializer


# Create your views here.

class ProxyList(APIView):
    """
    List all proxies, or create a new proxy.
    """
    def get(self, request, format=None):
        proxies = Proxy.objects.all()
        serializer = ProxySerializer(proxies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProxySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProxyDetail(APIView):
    """
    Retrieve, update or delete a code proxy.
    """
    def get_object(self, pk):
        try:
            return Proxy.objects.get(pk=pk)
        except Proxy.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        proxy = self.get_object(pk)
        serializer = ProxySerializer(proxy)
        return Response(serializer.data)

    def put(self, request, format=None):
        proxy = self.get_object(pk)
        serializer = ProxySerializer(proxy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        proxy = self.get_object(pk)
        proxy.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
