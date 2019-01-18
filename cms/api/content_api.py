from django.http import HttpResponse
from rest_framework.views import APIView

from common.attr_helper import getTime
from common.filter_helper import filterContent
from common.param_helper import getDictByPostRequest


class CMSContentApi(APIView):
    @getTime
    def post(self, request):
        obj = getDictByPostRequest(request)
        obj['content'] = filterContent(obj['content'])
        return HttpResponse({'status': 2})

    def get(self, request):
        print(request)
        return {'status': 1}
