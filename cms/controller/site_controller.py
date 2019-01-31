import json
from django.http import HttpResponseNotFound
from django.views import View
from django.shortcuts import render
from cms.ibiz.i_site_biz import ISiteBiz


class CMSListSiteController(View):
    def get(self, request):
        siteModel = ISiteBiz()().getByUrl(request.path)
        if siteModel is None:
            return HttpResponseNotFound("None")
        siteId = siteModel.id
        return render(request, 'dashboard.html', {'id': siteId})
