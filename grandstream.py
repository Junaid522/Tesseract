from datetime import datetime

from urllib3.exceptions import InsecureRequestWarning

import requests, ssl, json, hashlib
from requests.auth import HTTPDigestAuth

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

username = "cdrapi"
password = "cdrapi123B2C3Ni"
req_headers = {"Content-Type": "application/json"}


# 'Connection': 'close'
# }

def login(url):
    data = {
        "request": {
            "action": "challenge",
            "user": username,
            "version": "1.0"
        }
    }
    res = requests.post(url, data=json.dumps(data), headers=req_headers, verify=False)

    if res.status_code == 200:
        print(res.content)
    if res.status_code == 200:
        r = json.loads(res.text)
        if r['status'] == 0:
            challenge = r['response']['challenge']
            p = challenge + password
            token = hashlib.md5(p.encode('utf-8')).hexdigest()
            print(token)
            data2 = {
                "request": {
                    "action": "login",
                    "token": token,
                    "url": "https://72.137.146.94:8089/api",
                    "user": username
                }
            }
            res = requests.post(url, data=json.dumps(data2), headers=req_headers, verify=False)
            if res.status_code == 200:
                r = json.loads(res.text)
                if r['status'] == 0:
                    api_cookie = r['response']['cookie']
                    print('API Cookie is => {0}'.format(api_cookie))
                    return api_cookie
                else:
                    print('Login: Status => {0}'.format(r['status']))
                    print(r)
            else:
                print('Login Request Failed')
    else:
        print('Challenge Request Failed')
    return False


def getSystemGeneralStatus(url, api_cookie):
    # data = {
    #     "request": {
    #         "action": "getSystemGeneralStatus",
    #         "cookie": api_cookie
    #     }
    # }
    # data = {
    #     "request": {
    #         "action": "listAccount",
    #         "cookie": api_cookie,
    #         "item_num": "30", "options": "extension,account_type,fullname,status,addr", "page": "1",
    #         "sidx": "extension",
    #         "sord": "asc"
    #     }
    # }
    data = {
        "request": {
            "action": "cdrapi",
            "cookie": api_cookie,
            "format": "json"
        }
    }
    res = requests.post(url, data=json.dumps(data), headers=req_headers, verify=False)
    print(res.text)
    if res.status_code == 200:
        r = json.loads(res.text)
        if r['status'] == 0:
            print(res.content)
            print(r)
        else:
            print('getSystemGeneralStatus: Status => {0}'.format(r['status']))
            print(r)
    else:
        print('getSystemGeneralStatus Command Failed')


if __name__ == '__main__':
    url = 'https://72.137.146.94:8089/api'
    api_cookie = login(url)
    if api_cookie:
        getSystemGeneralStatus(url, api_cookie)
    # get_cdr_logs()
    # get_cdr_logs_incoming()
    # get_cdr_logs_incoming_voice_mails()

# curl - H "Content-Type: application/json;charset=UTF-8" - X POST - d '{"request": {"action": "challenge", "user": "cdrapi", "version": "1.0"}}' - k "https://72.137.146.94:8089/api" - -insecure
# curl -H "Content-Type: application/json;charset=UTF-8" -X POST -d '{"request": {"action":"login", "token":"10a42d3c3cd08ea006ae2d62c0e0b8bd", "url":"https://72.137.146.94:8089/api", "user":"cdrapi"}}' -k "https://72.137.146.94:8089/api" --insecure
#                                                                     {"request": {"action": "login", "token": "d89f91f7bd2a4d049b2ca4d05e380db6", "url":"https://72.137.146.94:8089/cdrapi?format=JSON", "user": "cdrapi"}}
