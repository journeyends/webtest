import json

from django.http import HttpResponse
from rest_framework.views import APIView

from cms.ibiz.i_channel_biz import IChannelBiz
from common.path_helper import addPath


class CMSListChannelApi(APIView):
    def get(self, request, sid):
        channelList = IChannelBiz()().getListBySiteId(sid)

        if channelList is not None:
            for channel in channelList:
                addPath(r'^/api/site/get/(?P<id>\d+)/$', CMSListChannelApi)

        result = json.dumps(list(channelList), ensure_ascii=False)
        return HttpResponse(result)
