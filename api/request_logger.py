"""
Module for logging requests
"""
import time

from flask import g, request

def add_request_logging(app):
    """
    Intercepts every flask request and logs in the following format:
    method=POST path=/api/v1/predict status=200 duration=0.0028 ip=172.17.0.1 host=localhost params={}
    /metrics and /api/v1/health endpoints are excluded to save having to many logs
    """

    @app.before_request
    def start_timer(): # pylint: disable=unused-variable,E0237
        g.start = time.time() # pylint: disable=E0237


    @app.after_request
    def log_request(response): # pylint: disable=unused-variable
        if request.path == '/metrics':
            return response

        if request.path == '/api/v1/health':
            return response

        now = time.time()
        duration = round(now - g.start, 4)

        ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
        host = request.host.split(':', 1)[0]
        args = dict(request.args)

        log_params = [
            ('method', request.method),
            ('path', request.path),
            ('status', response.status_code),
            ('duration', duration),
            ('ip', ip_address),
            ('host', host),
            ('params', args)
        ]

        request_id = request.headers.get('X-Request-ID')
        if request_id:
            log_params.append(('request_id', request_id))

        parts = []
        for name, value in log_params:
            part = "{}={}".format(name, value)
            parts.append(part)
        line = " ".join(parts)

        app.logger.info(line)

        return response
