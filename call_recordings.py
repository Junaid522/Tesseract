import csv
import datetime

from urllib3.exceptions import InsecureRequestWarning

import requests, ssl, json
from requests.auth import HTTPDigestAuth

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

username = 'cdrapi'
password = 'cdrapi1231'


def get_cdr_logs():
    now = datetime.datetime.now()
    date_time = now.strftime("%Y-%m-%dT%H:%M:%S-06:00")
    print(date_time)
    # url = 'https://72.137.146.94:8443/cdrapi?format=JSON&startTime=2020-04-11T00:00:00-06:00&endTime=2020-04-11T23:59:59-06:00'
    # url = 'https://72.137.146.94:8443/cdrapi?format=JSON&caller=9052775996&startTime=2020-03-01T00:00:00-06:00&endTime=2020-04-11T23:59:59-06:00'
    # url = 'https://72.137.146.94:8443/cdrapi?format=JSON&callee=9052775996&startTime=2019-03-01T00:00:00-06:00&endTime=2020-04-11T23:59:59-06:00'
    # url = 'https://72.137.146.94:8443/cdrapi?format=JSON&caller=1000&startTime=2020-03-01T00:00:00-06:00&endTime=2020-04-11T23:59:59-06:00'
    # url = 'https://72.137.146.94:8443/cdrapi?format=JSON&caller=1000&caller=1001&caller=1002&caller=1003&caller=1004&startTime=2020-03-01T00:00:00-06:00&endTime=2020-04-11T23:59:59-06:00'
    # url = 'https://72.137.146.94:8443/cdrapi?format=JSON&caller=1000&caller=1001&caller=1002&startTime=2020-03-01T00:00:00-06:00&endTime=2020-04-11T23:59:59-06:00'
          # 'caller=1000&caller=1001&caller=1002&' \
    # 'https://72.137.146.94:8443/recapi'
    url = 'https://72.137.146.94:8443/cdrapi?format=JSON&callee=1000&startTime=2020-03-01T00:00:00-06:00&endTime='+ date_time
    try:
        r = requests.get(url, auth=HTTPDigestAuth(username, password), verify=False)
        data = json.loads(r.content)
        # print(len(data['cdr_root']))
        # import pdb; pdb.set_trace()
        for d in data['cdr_root']:
            # print(d)
            # print('SOURCE: ',d.get('src'))
            # start = datetime.datetime.strptime(d.get('start'), '%Y-%m-%d %H:%M:%S')
            # end = datetime.datetime.strptime(d.get('end'), '%Y-%m-%d %H:%M:%S')
            # print('START: ', start)
            # print('END: ',end)
            # print(type(end))
            if d.get('recordfiles'):
                print('RECORDINGS: ', d.get('recordfiles'))
                # print(d)
            # print('RECORDINGS: ', d.get('recordfiles'))
            #     url = 'https://72.137.146.94:8443/recapi?filedir=monitor&filename={}'.format(d.get('recordfiles'))
            #     response = requests.get(url, auth=HTTPDigestAuth(username, password), verify=False)
            #     name = d.get('recordfiles').split('/')[1].replace('@', '')
            #     file = open(name, "wb")
            #     file.write(response.content)
            #     file.close()
            # if 'VoiceMailMain' == d.get('lastapp'):
            #     print('LAST APP: ',d.get('lastapp'))
            #     print('RECORDINGS: ', d.get('recordfiles'))
            #     print(d)
        # print(data)
        return data

    except:
        print('Nothing')
        return None


def get_all_cdr_logs():
    data = get_cdr_logs()
    if data:
        cdr_list = data['cdr_root']
        for item in cdr_list:
            if len(item) == 33:
                # if item['recordfiles']:
                #     save_recordings(item)
                # else:
                print("33: ", item['start'], item['end'])
                start_date = datetime.datetime.strptime(item['start'], '%Y-%m-%d %H:%M:%S')
                if item['end']:
                    end_date = datetime.datetime.strptime(item['end'], '%Y-%m-%d %H:%M:%S')
            else:
                cdr = ''
                for key, value in item.items():
                    if key == 'cdr':
                        cdr = item['cdr']

                    if not key == 'cdr':

                        # if value['recordfiles']:
                        #     save_update_recordings(value, cdr, phone_directory_object)
                        # else:
                        print("44:", value['start'], value['end'])
                        start_date = datetime.datetime.strptime(value['start'], '%Y-%m-%d %H:%M:%S')
                        if value['end']:
                            end_date = datetime.datetime.strptime(value['end'], '%Y-%m-%d %H:%M:%S')
                        # phone_directory_object.cdr = cdr
                        # phone_directory_object.dst = value['dst']
                        # phone_directory_object.lastdata = value['lastdata']
                        # phone_directory_object.duration = value['duration']
                        # phone_directory_object.disposition = value['disposition']
                        # phone_directory_object.answer = start_date
                        # phone_directory_object.recordfiles = value['recordfiles']
                        # phone_directory_object.end = end_date
                        # phone_directory_object.save()


if __name__ == "__main__":
    # get_all_cdr_logs()
    get_cdr_logs()
