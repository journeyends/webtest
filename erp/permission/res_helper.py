from erp.dal.sys_res_dal import SysResDal
from webtest import settings


def getRes(url, userId):
    sysResByDefaultUrl = SysResDal().getByDefaultUrl(url)
    resListByParentId = SysResDal().getListByParentId(sysResByDefaultUrl.res_id,
                                                      settings.SYSTEMID,
                                                      userId)
    formModel = {
        "ResID": sysResByDefaultUrl.res_id,
        "ResUrl": sysResByDefaultUrl.default_url,
        "ButtonViewVisible": False,
        "ButtonAddVisible": False,
        "ButtonEditVisible": False,
        "ButtonDeleteVisible": False,
        "ButtonPrintVisible": False,
        "ButtonCheckVisible": False,
        "ButtonCancelVisible": False,
        "ButtonFinishVisible": False,
        "ButtonExtendVisible": False
        }

    for res in resListByParentId:
        if res.button_type == 1:
            formModel["ButtonViewVisible"] = True
        elif res.button_type == 2:
            formModel["ButtonAddVisible"] = True
        elif res.button_type == 3:
            formModel["ButtonEditVisible"] = True
        elif res.button_type == 4:
            formModel["ButtonDeleteVisible"] = True
        elif res.button_type == 5:
            formModel["ButtonPrintVisible"] = True
        elif res.button_type == 6:
            formModel["ButtonCheckVisible"] = True
        elif res.button_type == 7:
            formModel["ButtonCancelVisible"] = True
        elif res.button_type == 8:
            formModel["ButtonFinishVisible"] = True
        elif res.button_type == 9:
            formModel["ButtonExtendVisible"] = True

    return formModel
