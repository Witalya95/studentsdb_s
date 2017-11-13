from datetime import datetime

from django.http import HttpResponse


class RequestTimeMiddleware(object):
    """Display request time on a page"""


    def __init__(self, get_response):
        self.get_response = get_response
    # One-time configuration and initialization.


    def __call__(self, request):
    # Code to be executed for each request before
    # the view (and later middleware) are called.

        request.start_time = datetime.now()

        response = self.get_response(request)

        request.end_time = datetime.now()
        response.write('<br />Request took:' + str(request.end_time - request.start_time))

    # Code to be executed for each request/response after
    # the view is called.

        return response


