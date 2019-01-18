from erp.controller.contact_unit_controller import ContactUnitApi,ContactUnitRestApi
from erp.controller.home import Home

from django.urls import path

from erp.controller.salesInfoPreController import SalesInfoPreDetailApi, SalesInfoPreSaveOrUpdateApi

urlpatterns = []

urlpatterns += [
    path('home/', Home.as_view()),
    path('contactUnitApi/', ContactUnitApi.as_view()),
    path('salesInfoPre/getById/', SalesInfoPreDetailApi.as_view()),
    path('salesInfoPre/save/', SalesInfoPreSaveOrUpdateApi.as_view()),
]

