def app(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    response_headers = [
        ('Content-type','text/plain')]
        #,('Content-Length', str(len(resp)))]
    start_response(status, response_headers)
    resp = environ['QUERY_STRING'].split("&")
    resp = [item+"\n" for item in resp]
    return resp
