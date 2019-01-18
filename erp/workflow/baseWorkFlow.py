import json

from django.db.models.base import ModelBase

from erp.common.api_helper import post
from erp.common.format_helper import strFormat
from erp.common.serialize_helper import modelToJson, DecimalEncoder
from erp.ibiz.i_sys_org_biz import I_sys_org_biz
from erp.permission.res_helper import getRes
from erp.workflow.erpWorkFlow import ErpWorkFlow
from django.http import HttpResponse


def injectedClass():
    return ErpWorkFlow


class BaseWorkFlowMapper(type):
    def __call__(cls, *args, **kwargs):
        injected_class = injectedClass()
        obj = injected_class.__new__(injected_class, *args, **kwargs)
        obj.__init__(*args, **kwargs)
        return obj


class BaseWorkFlow(metaclass=BaseWorkFlowMapper):
    pass


def getHttpResponseWorkflow(result, request, key_id, create_user_id,
                            is_post, check_status, url='', dept_id=0):
    if url == '':
        url = request._request.META['PATH_INFO'].strip('/')

    menu = getRes(url, request.current_user_id)
    result.update({'FormModel': menu})

    workflow = {"MenuID": menu.get("ResID"), "MenuURL": menu.get("ResUrl")}

    if dept_id == 0:
        if create_user_id > 0:
            org = I_sys_org_biz().instance().getOrgByUserId(create_user_id)
        else:
            org = I_sys_org_biz().instance().getOrgByUserId(request.current_user_id)
        workflow["DeptID"] = org['org_id']

    workflow["CurrentUser"] = request.current_user_id
    workflow["KeyID"] = key_id
    workflow["SubmitPrefix"] = url

    workflowResponse = post(workflow, url='172.21.202.34:24806')
    workflowStr = strFormat(workflowResponse.decode('utf-8'))
    workflowResult = eval(workflowStr)

    if ModelBase in [type(p) for p in type(result).__bases__]:
        result = modelToJson(result)

    if isinstance(result, str):
        result = eval(strFormat(result))

    if isinstance(result, dict):
        result.update({'WorkFlow': workflowResult})

    content = json.dumps(result, ensure_ascii=False, cls=DecimalEncoder)
    return HttpResponse(content)
