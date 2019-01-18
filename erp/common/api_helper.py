import http.client
import json


def post(param, url='172.21.202.34:24806', content_type="json"):
    contentType = "application/json"

    if content_type == "json":
        contentType = "application/json"
    elif content_type == "urlencoded":
        contentType = "application/x-www-form-urlencoded"

    conn = http.client.HTTPConnection(url)

    payload = {}

    if isinstance(param, dict):
        payload = json.dumps(param).encode(encoding='utf-8')
    elif isinstance(param, str):
        payload = param

    headers = {
        'content-type': contentType
    }

    conn.request("POST", "/api/WF/InitWFController", payload, headers)

    res = conn.getresponse()
    data = res.read()
    return data


if __name__ == '__main__':
    post({"KeyID": 5007694, "DeptID": 6987, "MenuID": "10000052050422"})
