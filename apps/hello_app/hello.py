def application(environ, start_response):
    """The simplest WSGI application that prints its own query string.""" 
    data = bytes('\n'.join(environ['QUERY_STRING'].split('&')), encoding='utf8')
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])
