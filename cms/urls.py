import json
from django.conf.urls import url
from django.urls import path

from cms.api.category_api import CMSCategoryListApi
from cms.api.content_api import CMSContentApi, CMSContentListApi
from cms.controller.channel_controller import CMSChannelController
from cms.controller.content_controller import CMSContentController
from cms.ibiz.i_channel_biz import IChannelBiz
from cms.ibiz.i_site_biz import ISiteBiz
from cms.api.channel_api import CMSListChannelApi, CMSChannelApi
from cms.api.site_api import CMSGetSiteApi, CMSListSiteApi, CMSSiteApi
from cms.controller.site_controller import CMSListSiteController

urlpatterns = []

urlpatterns += [
    url(r'^/api/site/get/(?P<id>\d+)', CMSGetSiteApi.as_view()),
    url(r'^/api/site/first', CMSSiteApi.as_view()),
    path('/api/site/list', CMSListSiteApi.as_view()),
]

obj = ISiteBiz()().getSiteList()
siteList = eval(json.dumps(list(obj), ensure_ascii=False))
urlpatterns += [path(p["path"], CMSListSiteController.as_view()) for p in siteList]

urlpatterns += [
    url(r'^/api/channel/first', CMSChannelApi.as_view()),
    url(r'^/api/channel/list', CMSListChannelApi.as_view())
]

channelObj = IChannelBiz()().getChannelList()
if channelObj is not None:
    channelList = eval(json.dumps(list(channelObj), ensure_ascii=False))
    urlpatterns += [path(p["path"], CMSChannelController.as_view()) for p in channelList]

urlpatterns += [
    url(r'^/api/category/list', CMSCategoryListApi.as_view()),
]

urlpatterns += [
    url(r'^/content/(?P<cid>\d+)', CMSContentController.as_view()),
    url(r'^/api/content/first', CMSContentApi.as_view()),
    url(r'^/api/content/list', CMSContentListApi.as_view()),
]