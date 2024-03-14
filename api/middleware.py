import logging
from django.http import HttpRequest, HttpResponse

from api.models import Log


class CustomLogHandler(logging.Handler):
    def emit(self, record):
        try:
            log = Log(**record.__dict__["msg"])
            log.save()
        except Exception as e:
            print("EXCEPTION: ", e)


logging.basicConfig(handlers=[CustomLogHandler()], level=logging.INFO)

logger = logging.getLogger(__name__)


class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        print("Custom Middleware Called")
        if not request.path.startswith("/api/todos/"):
            return self.get_response(request)
        request_body = request.body.decode("utf-8")
        headers = str(request.headers)
        method = request.method
        path = request.path
        user = request.user.username
        ip_address = request.META.get("REMOTE_ADDR")
        params = {
            "request_body": request_body,
            "headers": headers,
            "method": method,
            "path": path,
            "user": user,
            "ip_address": ip_address,
        }
        response: HttpResponse = self.get_response(request)
        params["status"] = response.status_code
        params["response_body"] = response.content.decode("utf-8")
        try:
            logger.info(params)
        except Exception as e:
            print("EXCEPTION: ", e)
        return response
