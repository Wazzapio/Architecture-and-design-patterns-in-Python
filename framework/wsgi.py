from framework.request import Request
from framework.view import View
from framework.render import render


class Framework:

    def __init__(self, urls):
        self.urls = urls

    def __call__(self, environ, start_response):
        request = Request(environ)
        view = self._get_view(request)
        print(self._get_response(request, view))
        template = self._get_template(request)
        start_response('200 OK', [('Content-Type', 'text/html')])
        print(render(template))
        return [b'Hello world from a simple WSGI application!']


    def _get_view(self, request: Request):
        path = request.path
        for url in self.urls:
            if url.path == path:
                return url.view
        return None

    def _get_response(self, request: Request, view: View):
        if hasattr(view, request.method):
            return getattr(view, request.method)(view, request)
        return 'Метод не поддерживается'

    def _get_template(self, request: Request):
        path = request.path
        for url in self.urls:
            if url.path == path:
                return url.template
        return None
