from cms.entity.site_entity import SiteModel


class SiteDal:
    def getById(self, id):
        obj = SiteModel.objects.filter(id=id).first()
        return obj

    def getList(self):
        obj = SiteModel.objects.all().values('id', 'name', 'path', 'is_on')
        return obj

    def getSiteList(self):
        obj = SiteModel.objects.filter(is_on=1).values('id', 'name', 'path', 'is_on')
        return obj

    def getByPath(self, path):
        obj = SiteModel.objects.filter(path=path).first()
        return obj