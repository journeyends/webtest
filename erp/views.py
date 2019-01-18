from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def page_not_found(request, exception, template_name=''):
    res = HttpResponse("page not found")
    res.status_code = 404
    return res