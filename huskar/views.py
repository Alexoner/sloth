import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
#  from huskarAdmin.models import Snippet
#  from huskarAdmin.serializers import SnippetSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        #  snippets = Snippet.objects.all()
        #  serializer = SnippetSerializer(snippets, many=True)
        #  return JSONResponse(serializer.data)
        d = {"a": "b"}
        return JSONResponse(d)


    #  elif request.method == 'POST':
        #  data = JSONParser().parse(request)
        #  serializer = SnippetSerializer(data=data)
        #  if serializer.is_valid():
            #  serializer.save()
            #  return JSONResponse(serializer.data, status=201)
        #  return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    #  try:
        #  snippet = Snippet.objects.get(pk=pk)
    #  except Snippet.DoesNotExist:
        #  return HttpResponse(status=404)

    if request.method == 'GET':
        #  serializer = SnippetSerializer(snippet)
        #  return JSONResponse(serializer.data)
        d = {"a": "b"}
        return JSONResponse(json.dumps(d))

    #  elif request.method == 'PUT':
        #  data = JSONParser().parse(request)
        #  serializer = SnippetSerializer(snippet, data=data)
        #  if serializer.is_valid():
            #  serializer.save()
            #  return JSONResponse(serializer.data)
        #  return JSONResponse(serializer.errors, status=400)

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
        #  serializer = SnippetSerializer(snippet)
        #  return JSONResponse(serializer.data)
        #  return JSONResponse(json.dumps(d))
        if pk:
            with open('data/query_one.json?id=%s.json' % (pk)) as f:
                data = f.read()
                kwargs = {}
                kwargs['content_type'] = 'application/json'
                return HttpResponse(data, **kwargs)
        else:
            return HttpResponse('This is the list of libraries, query params: %s' % request.GET.get('a'))

