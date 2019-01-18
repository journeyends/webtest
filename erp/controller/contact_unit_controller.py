from django.shortcuts import HttpResponse
from django.views import View
from django.http import JsonResponse
import json

from rest_framework.views import APIView

from erp.common.serialize_helper import DecimalEncoder


class ContactUnitApi(APIView):
    def get(self, request):
        from erp.ibiz.i_contact_unit_biz import I_contact_unit_biz
        biz = I_contact_unit_biz().instance()
        data = biz.getList(condition=request.GET.dict(), user_info=request.session_manager)
        print(type(data))
        datalist = json.dumps(dict(data), ensure_ascii=False, cls=DecimalEncoder)
        return HttpResponse(datalist)

class ContactUnitRestApi(APIView):
    # get 请求
    def get(self, request):
        # 获取参数数据
        get = request.GET
        # 获取参数 a
        a = get.get('Code')
        print(a)
        # 返回信息
        d = {
            'status': 1,
            'message': 'success',
            }
        return JsonResponse(d)
