"""
Clickjacking Protection Middleware.

This module provides a middleware that implements protection against a
malicious site loading resources from your site in a hidden frame.
"""

from django.conf import settings

ACCESS_CONTROL_ALLOW_PREFIX = 'Access-Control-Allow-'

class CORSMiddleware(object):

    def process_response(self, request, response):
        # Don't set it if it's already in the response
        if response.get('%sCredentials'%(ACCESS_CONTROL_ALLOW_PREFIX)) is not None:
            return response
        else:
            response['%sCredentials'%(ACCESS_CONTROL_ALLOW_PREFIX)] = True

        if response.get('%sHeaders'%(ACCESS_CONTROL_ALLOW_PREFIX)) is not None:
            return response
        else:
            response['%sHeaders'%(ACCESS_CONTROL_ALLOW_PREFIX)] = 'Content-Type'
            pass

        if response.get('%sMethods'%(ACCESS_CONTROL_ALLOW_PREFIX)) is not None:
            return response
        else:
            response['%sMethods'%(ACCESS_CONTROL_ALLOW_PREFIX)] = 'GET, POST, PUT, DELETE, OPTIONS'
            pass

        if response.get('%sOrigin'%(ACCESS_CONTROL_ALLOW_PREFIX)) is not None:
            return response
        else:
            response['%sOrigin'%(ACCESS_CONTROL_ALLOW_PREFIX)] = 'localhost:8000'
            pass

        # Don't set it if they used @xframe_options_exempt
        if getattr(response, 'xframe_options_exempt', False):
            return response

        return response
