from cms.idal.i_site_dal import ISiteDal


class SiteBiz:
    dal = ISiteDal()()

    def getList(self):
        dal = SiteBiz.dal
        return dal.getList()

    def getById(self, id):
        dal = SiteBiz.dal
        return dal.getById(id)

    def getSiteList(self):
        dal = SiteBiz.dal
        return dal.getSiteList()

    def getByPath(self, path):
        dal = SiteBiz.dal
        return dal.getByPath(path)
