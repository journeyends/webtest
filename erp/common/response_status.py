from django.http import HttpResponse

def http401(msg="Unauthorized"):
    res = HttpResponse(msg)
    res.status_code = 401
    return res
