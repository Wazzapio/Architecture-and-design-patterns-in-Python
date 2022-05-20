class Request:
    def __init__(self, environ):
        self.method = environ['REQUEST_METHOD'].lower()
        self.path = environ['PATH_INFO']
        self.headers = self._get_headers(environ)
        self.wsgi_input = environ['wsgi.input'].read().decode('utf-8')
        self.query_params = self._get_query_params(environ)

    def _get_headers(self, environ):
        headers = {}
        for key, value in environ.items():
            if key.startswith('HTTP_'):
                headers[key[5:].lower()] = value
        return headers

    def _get_query_params(self, environ):
        query_params = {}
        qs = environ.get('QUERY_STRING')
        if not qs:
            return {}
        qs = qs.split('&')
        for q_str in qs:
            key, value = q_str.split('=')
            if query_params.get(key):
                query_params[key].append(value)
            query_params[key] = [value]
        return query_params
