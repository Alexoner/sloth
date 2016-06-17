import json
import os
import sys
from subprocess import call

from rest_framework import status
from rest_framework.views import APIView
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404

class GitHubHookView(APIView):
    """
    GitHub web post-hook service
    """
    config = None

    @classmethod
    def getConfig(cls):
        # TODO: refinement. not used yet
        if(cls.config is None):
            # try:
                # configString = open(cls.CONFIG_FILEPATH).read()
            # except:
                # sys.exit('Could not load ' + cls.CONFIG_FILEPATH + ' file')

            try:
                cls.config = {
                    'repositories': [
                        {
                            'url': 'https://github.com/Alexoner/sloth',
                            'path': '/root/src/sloth/',
                        }
                    ]
                }
            except:
                sys.exit(' file is not valid json')

        return cls.config

    def post(self, request):
        # event = request.META.get('X-GitHub-Event')
        # if event == 'ping':
            # return Response(status=status.HTTP_204_NO_CONTENT)
        # if event != 'push':
            # return Response(status=status.HTTP_304_NOT_MODIFIED)

        url = self.parse_request(request)
        paths = self.getMatchingPaths(url)
        for path in paths:
            self.git_fetch(path, url)
            self.deploy(path)

        return Response('ok', status=status.HTTP_200_OK)

    @classmethod
    def parse_request(cls, request):
        payload = request.body
        data = json.loads(payload.decode())
        return data['repository']['url']

    def getMatchingPaths(self, repoUrl):
        res = []
        config = self.getConfig()
        for repository in config['repositories']:
            if(repository['url'] == repoUrl):
                res.append(repository['path'])
        return res

    @classmethod
    def git_fetch(cls, path, url):
        print('fetching %s into %s' % (url, path))
        if not os.path.exists(path):
            # os.mkdir(path)
            call('mkdir -p %s' % (path), shell=True)
            call('cd %s && git clone %s' % (path, url), shell=True)
        else:
            call('git fetch', shell=True)

    @classmethod
    def git_pull(cls, path):
        call('cd %s && git pull' % (path), shell=True)

    def deploy(self, path):
        config = self.getConfig()
        for repository in config['repositories']:
            if(repository['path'] == path):
                if 'deploy' in repository:
                    branch = None
                    if 'branch' in repository:
                        branch = repository['branch']

                    if branch is None:
                        # if(not self.quiet):
                            # print 'Executing deploy command'
                        call(['cd "' + path + '" && ' +
                              repository['deploy']], shell=True)
