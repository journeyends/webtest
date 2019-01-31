from cms.entity.channel_entity import ChannelModel


class ChannelDal:
    def getListBySiteId(self, siteId):
        obj = ChannelModel.objects.filter(is_on=1, site_id=siteId)\
            .values('id', 'name', 'path', 'parent_id')
        return obj

    def getChannelList(self):
        obj = ChannelModel.objects.filter(is_on=1).values('id', 'name', 'path', 'parent_id')
        return obj

    def getChannelByPath(self, path):
        obj = ChannelModel.objects.filter(path=path).first()
        return obj

    def getById(self, id):
        obj = ChannelModel.objects.filter(id=id).first()
        return obj