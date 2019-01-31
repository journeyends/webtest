import json

from django.http import HttpResponse
from rest_framework.views import APIView

from cms.ibiz.i_site_biz import ISiteBiz
from common.serialize_helper import modelToJson


class CMSGetSiteApi(APIView):
    def get(self, request, id):
        siteModel = ISiteBiz()().getById(id)
        result = modelToJson(siteModel)
        print(type(result))
        return HttpResponse(result)

    def post(self, request):
        pass


class CMSSiteApi(APIView):
    def get(self, request):
        sitePath = request.GET.get("sitePath")
        if sitePath is not None:
            siteModel = ISiteBiz()().getByUrl(sitePath)
            result = modelToJson(siteModel)
        return HttpResponse(result)


class CMSListSiteApi(APIView):
    def get(self, request):
        obj = ISiteBiz()().getList()
        result = json.dumps(list(obj), ensure_ascii=False)
        print(type(result))
        return HttpResponse(result)
