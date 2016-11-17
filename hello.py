def app(environ, start_response):
    request_method = environ['REQUEST_METHOD']
    if request_method == 'GET':
        query_string = environ['QUERY_STRING']
        params = query_string.split('?')
        for param in params:
            response_body= response_body + param + '\r\n'
        status = '200 OK'
        response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
        ]
        start_response(status, response_headers)
        return [response_body]
