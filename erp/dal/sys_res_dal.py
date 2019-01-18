from erp.common.common_search import getListBySql
from erp.entity.sys_res import SysRes


class SysResDal:
    def getById(self, id=0):
        obj = SysRes.objects.filter(res_id=id).first()
        return obj

    def getByDefaultUrl(self, defaultUrl):
        obj = SysRes.objects.filter(default_url=defaultUrl).first()
        return obj

    def getListByParentId(self, res_id, system_id, current_user_id):
        obj = getListBySql(sql="SELECT   A.RESID, A.RESNAME, A.ALIAS, A.SN,A.ICON_CLASS as ICON, A.PARENTID, A.DEFAULTURL, A.ISFOLDER, A.ISDISPLAYINMENU, A.ISOPEN,\
                              A.ISNEWOPEN, A.PATH, A.IS_COMMON, A.IS_ONLY_HYPERLINK, A.IS_BUTTON,A.BUTTON_TYPE\
                              FROM     sys_res A\
                              INNER JOIN sys_subsystem B ON A.SYSTEMID = B.SYSTEMID\
                              INNER JOIN sys_role_res C ON A.RESID = C.RESID\
                              INNER JOIN sys_role D ON C.ROLEID = D.ROLEID\
                              INNER JOIN sys_user_role E ON D.ROLEID = E.ROLEID\
                              INNER JOIN sys_user F ON E.USERID = F.USERID\
                              WHERE    A.IS_BUTTON = 1 AND B.SYSTEMID = {_system_id} AND F.USERID = {_current_user_id} AND F.STATUS = 1 AND A.PARENTID={_res_id}\
                              ORDER BY A.SN ".format(_current_user_id=str(current_user_id), _res_id=str(res_id), _system_id=str(system_id)))
        return obj