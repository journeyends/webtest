from django.views import View
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core import serializers
from rest_framework import serializers
from erp.entity.vw_sys_contact_unit import ContactUnit
import json

class Home(View):
    def get(self, request):
        obj = ContactUnit.objects.all()[0:10].values('unit_id', 'unit_name')

        data1 = json.dumps(list(obj), ensure_ascii=False)
        # print(request.session_manager['account'])
        return HttpResponse(data1)

    def post(self, request):
        print('fuck')
        return HttpResponse('fuck')
