import datetime

from django.utils import timezone
from urllib3.exceptions import InsecureRequestWarning

import requests, ssl, json, hashlib
from requests.auth import HTTPDigestAuth
import pandas as pd

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
    now = datetime.datetime.now()
    date_time = now.strftime("%Y-%m-%dT%H:%M:%S-06:00")

    data = {
        "request": {
            "action": "cdrapi",  # it will fetch phone records, or recordfile mey file ka name hoga in case of voicemail
            # "action": "recapi", # it will fetch audio files if exists, phr hum append kren gy rec api mey name ko
            "cookie": api_cookie,
            "format": "json",
            # "filedir": "voicemail",
            # "filedir": "meetme"
            # "filename": "auto-1589836368-1000-011972595610600.wav"
            "startTime": "2021-03-01T00:00:00-06:00",
            "endTime": date_time,
            "callee": "1000"
        }

        # "request": {
        #     "action": "recapi", "cookie": api_cookie, "filedir": "monitor"
        # }
    }
    res = requests.post(url, data=json.dumps(data), headers=req_headers, verify=False)
    # print(res.content)
    if res.status_code == 200:
        r = json.loads(res.text)
        print(r)
    #     if r:
    #         cdr_list = r['cdr_root']
    #         for index, item in enumerate(cdr_list):
    #             # if index == 0:
    #             #     print(item)
    #             if len(item) == 33:
    #                 # print(item['clid'])
    #                 if item['lastapp'] == 'VoiceMail':
    #                     print(item['lastapp'])
    #                 else:
    #                     print(item['recordfiles'])
    #             else:
    #                 cdr = ''
    #                 for key, value in item.items():
    #                     if key == 'cdr':
    #                         cdr = item['cdr']
    #
    #                     if not key == 'cdr':
    #                         # if 'clid' in item.keys():
    #                         #     print(item['caller_name'])
    #                         if 'lastapp' in item.keys():
    #                             print(item['lastapp'])
    #                         else:
    #                             print(value['recordfiles'])
        # print(res.content)
        # Serializing json
        # json_object = json.dumps(res.text, indent=4)

        # Writing to sample.json
        # with open("grandstream_updated_0.json", "w") as outfile:
        #     outfile.write(res.text)
        # if r['status'] == 0:
        # for i in r.get('cdr_root'):
            # if i.get("lastdata") == "VoiceMailMain":
            # print('DATA', i.get("lastdata"))
            # print('DATA', i.get("recordfiles"))
        #     print(r)
        # else:
        #     print('getSystemGeneralStatus: Status => {0}'.format(r['status']))
        #     print(r)
    # else:
    #     print('getSystemGeneralStatus Command Failed')


def read_json():
    df = pd.read_json('grandstream_updated_0.json')
    df = df.get('cdr_root')
    data_list = []
    for index, d in enumerate(df):
        de = {}
        # if d.get('dst') in ['6400', '1001', '1002', '1003', '1004', '7000']:
        print(d.get('AcctId'))
        de['cdr'] = d.get('cdr')
        de['dst'] = d.get('dst')
        de['src'] = d.get('src')
        de['lastdata'] = d.get('lastdata')
        de['disposition'] = d.get('disposition')
        de['recordfiles'] = d.get('recordfiles')
        de['start'] = d.get('start')
        de['end'] = d.get('end')
        # print(de.get('recordfiles'))
        data_list.append(de)
        # if d.get('lastapp'):
        # if d.get('recordfiles'):
        #     print(index, d)
    print(len(data_list))


if __name__ == '__main__':
    url = 'https://72.137.146.94:8089/api'
    api_cookie = login(url)
    if api_cookie:
        getSystemGeneralStatus(url, api_cookie)
    # read_json()

    # get_cdr_logs()
    # get_cdr_logs_incoming()
    # get_cdr_logs_incoming_voice_mails()

# curl - H "Content-Type: application/json;charset=UTF-8" - X POST - d '{"request": {"action": "challenge", "user": "cdrapi", "version": "1.0"}}' - k "https://72.137.146.94:8089/api" - -insecure
# curl -H "Content-Type: application/json;charset=UTF-8" -X POST -d '{"request": {"action":"login", "token":"10a42d3c3cd08ea006ae2d62c0e0b8bd", "url":"https://72.137.146.94:8089/api", "user":"cdrapi"}}' -k "https://72.137.146.94:8089/api" --insecure
#                                                                     {"request": {"action": "login", "token": "d89f91f7bd2a4d049b2ca4d05e380db6", "url":"https://72.137.146.94:8089/cdrapi?format=JSON", "user": "cdrapi"}}
