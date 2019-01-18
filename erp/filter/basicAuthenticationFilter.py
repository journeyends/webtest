from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
import jwt
import time
from django.conf import settings
from erp.common.response_status import http401
from erp.common.redis_helper import getRedisLink


class BasicAuthenticationFilter(MiddlewareMixin):
    def process_request(self, request):
        http_authorization = request.META.get('HTTP_AUTHORIZATION')
        if http_authorization is None:
            return http401('no token')
        auth = http_authorization.split()
        if len(auth) < 2:
            return http401('wrong token')
        if auth[0] != 'Basic' and auth[0] != 'Jwt':
            return http401('defined token')
        token = auth[1]
        payload = jwt.decode(token, settings.SECRET_TOKEN, verify=False, algorithm=['HS256'])
        if 'exp' in payload.keys() is False:
            return http401('no exp token')
        timestamp_now = time.time()
        if timestamp_now > payload['exp']:
            return http401('expired token')
        redisHelper = getRedisLink()
        tokenInfo = redisHelper.get(token)
        if tokenInfo is None:
            return http401('error token')
        user_info = eval(tokenInfo.decode("utf-8"))
        request.session_manager = user_info
        request.current_user_id = user_info["USERID"]
        request.current_user_name = user_info["FULLNAME"]
        request.current_org_id = user_info["ORGID"]
        request.current_org_name = user_info["ORGNAME"]

    def process_response(self, request, response):
        return response
