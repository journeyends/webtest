import json
from django.conf.urls import url
from django.urls import path

from cms.api.content_api import CMSContentApi
from cms.controller.content_controller import CMSContentController
from cms.ibiz.i_site_biz import ISiteBiz
from cms.api.channel_api import CMSListChannelApi
from cms.api.site_api import CMSGetSiteApi, CMSListSiteApi
from cms.controller.site_controller import CMSListSiteController

urlpatterns = []

urlpatterns += [
    url(r'^/api/site/get/(?P<id>\d+)', CMSGetSiteApi.as_view()),
    path('/api/site/list', CMSListSiteApi.as_view()),
]

obj = ISiteBiz()().getSiteList()
siteList = eval(json.dumps(list(obj), ensure_ascii=False))
urlpatterns += [path(p["path"], CMSListSiteController.as_view()) for p in siteList]

urlpatterns += [
    url(r'^/api/channel/list/(?P<sid>\d+)', CMSListChannelApi.as_view()),
]

urlpatterns += [
    url(r'^/content/(?P<cid>\d+)', CMSContentController.as_view()),
    url(r'^/api/content', CMSContentApi.as_view()),
]