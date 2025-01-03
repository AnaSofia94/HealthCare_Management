import logging

logger = logging.getLogger(__name__)

class LogClientRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(f"Client IP: {get_client_ip(request)}, Endpoint: {request.path}, Method: {request.method}")
        return self.get_response(request)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip