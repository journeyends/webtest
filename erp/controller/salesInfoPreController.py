import datetime
import json
import time

from django.core import serializers
from django.db.models.base import ModelBase
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView

from erp.common.format_helper import strFormat
from erp.common.json_helper import bindModelByJson
from erp.common.model_helper import initEntityData
from erp.common.serialize_helper import modelToJson
from erp.dal.sys_res_dal import SysResDal
from erp.entity.sales_info_pre import SalesInfoPre

from erp.workflow.baseWorkFlow import BaseWorkFlow, getHttpResponseWorkflow


class SalesInfoPreDetailApi(APIView):
    def get(self, request):
        obj = SalesInfoPre.objects.filter(pre_id=1).first()
        from erp.ibiz.i_sys_org_biz import I_sys_org_biz
        a = I_sys_org_biz().instance().getOrgByUserId(25254)

        result = {'SalesInfoPre': eval(strFormat(modelToJson(obj)))}
        return getHttpResponseWorkflow(result, request, obj.pre_id, obj.create_user_id,
                                       obj.is_post, obj.check_status,
                                       url='/SalesManage/SalesInfoPre/Create')

class SalesInfoPreSaveOrUpdateApi(APIView):
    def post(self, request):
        obj = bindModelByJson(SalesInfoPre, eval(request.body))
        initEntityData(obj, request)
        obj.save()
        BaseWorkFlow('a')
        return HttpResponse("a")
