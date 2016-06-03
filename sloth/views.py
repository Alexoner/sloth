import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

from sloth.serializers import UserSerializer


# USER: ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset         = User.objects.all()
    serializer_class = UserSerializer

# class UserList(generics.ListAPIView):
    # queryset = User.objects.all()
    # serializer_class = UserSerializer

# class UserDetail(generics.RetrieveAPIView):
    # queryset = User.objects.all()
    # serializer_class = UserSerializer

##########################################################

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        # super().__init__(content, **kwargs)
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        d = {"a": "b"}
        return JSONResponse(d)

@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """

    if request.method == 'GET':
        d = {"a": "b"}
        return JSONResponse(json.dumps(d))
    elif request.method == 'DELETE':
        #  snippet.delete()
        return HttpResponse(status=204)

@csrf_exempt
def libraries(request,pk=None):
    """TODO: Docstring for libraries.

    :request: TODO
    :returns: TODO

    """
    if request.method == 'GET':
        if pk:
            with open('data/query_one.json?id=%s.json' % (pk)) as f:
                data = f.read()
                kwargs = {}
                kwargs['content_type'] = 'application/json'
                return HttpResponse(data, **kwargs)
        else:
            return HttpResponse('This is the list of libraries, query params: %s' % request.GET.get('a'))
