from framework.wsgi import Framework
from framework.url import Url
from framework.view import View


class MyFirstView(View):

    def get(self, request):
        return 'GET'

    def post(self, request):
        return 'POST'


urls = [
    Url('/', MyFirstView, 'framework/templates/index.html'),
    Url('/about', MyFirstView, 'framework/templates/about.html')
]

app = Framework(urls)
