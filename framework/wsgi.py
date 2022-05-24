from pprint import pprint

from framework.request import Request
from framework.view import View
from framework.render import render


class Framework:

    def __init__(self, urls):
        self.urls = urls

    def __call__(self, environ, start_response):
        # pprint(environ)
        request = Request(environ)
        view = self._get_view(request)
        response = self._get_response(request, view)
        template = self._get_template(request)
        print(render(template))
        start_response(response.status, list(response.headers.items()))
        return [response.body.encode()]

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
