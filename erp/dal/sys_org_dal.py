from erp.common.common_search import getListBySql


class Sys_org_dal:
    def getOrgByUserId(self, userId):
        obj = getListBySql(sql="SELECT so.ORGID org_id,so.ORGNAME org_name FROM sys_org so\
                                  INNER JOIN sys_user_pos sup ON so.ORGID=sup.ORGID\
                                  INNER JOIN sys_user su ON sup.USERID=su.USERID\
                                  WHERE su.USERID={_user_id}".format(_user_id=str(userId)))
        if len(obj) > 0:
            return obj[0]
        else:
            return None
