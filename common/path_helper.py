from django.conf.urls import url
from django.urls import path

path_name_list = []

def addPath(path, api):
    global path_name_list
    from cms.urls import urlpatterns
    if path in path_name_list:
        return False
    else:
        urlpatterns += [
            url(path, api.as_view()),
        ]
        path_name_list += [path]
        return True

