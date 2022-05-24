from framework.wsgi import Framework
from framework.url import Url
from framework.view import View
from framework.response import Response


class MyFirstView(View):

    def get(self, request):
        print('GET')
        return Response(body='GET SUCCESS')

    def post(self, request):
        print('POST')
        return Response(status='201 Created', body='POST SUCCESS', headers={'test': '123'})


urls = [
    Url('/', MyFirstView, 'framework/templates/index.html'),
    Url('/about', MyFirstView, 'framework/templates/about.html')
]

app = Framework(urls)
