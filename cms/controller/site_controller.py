import json
from django.http import HttpResponseNotFound
from django.views import View
from django.shortcuts import render
from cms.ibiz.i_site_biz import ISiteBiz


class CMSListSiteController(View):
    def get(self, request):
        if request.path.find('/cms') == 0:
            path = request.path[4:]
        else:
            return HttpResponseNotFound("None")
        siteModel = ISiteBiz()().getByPath(path)
        siteId = siteModel.id
        return render(request, 'index.html', {'id': siteId})
