from erp.idal.i_sys_org_dal import I_sys_org_dal


class Sys_org_biz:
    dal = I_sys_org_dal().instance()

    def getOrgByUserId(self, userId):
        dal = Sys_org_biz.dal
        return dal.getOrgByUserId(userId)
