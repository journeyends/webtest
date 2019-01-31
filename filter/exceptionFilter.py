from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from erp.common.log_helper import log


class ExceptionFilter(MiddlewareMixin):
    def process_exception(self, request, exception):
        log.logError(exception)
        res = HttpResponse(exception)
        res.status_code = 500
        return res

