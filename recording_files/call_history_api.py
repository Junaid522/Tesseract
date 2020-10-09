from urllib3.exceptions import InsecureRequestWarning

import requests ,ssl, json
from requests.auth import HTTPDigestAuth

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


# username = 'cdrapi'
# password = 'cdrapi1231'

username = 'tmna.rpad003@toyota.com'
password = "Pj;5b'kQIIpn"
# url = 'https://72.137.146.94:8443/cdrapi?format=JSON&caller=1000&numRecords=10'

# url = 'https://72.137.146.94:8443/recapi?filedir=voicemail?filename=unavail.wav'

# url = 'https://103.255.4.51:8443/recapi?filedir=meetme@monitor@voicemail/default'

# url = 'https://72.137.146.94:8443/recapi?filedir=meetme@monitor@voicemail/default'
url = 'https://myteams.toyota.com/sites/tmnascmdsm'

# url = 'https://72.137.146.94:8443/recapi?filedir=voicemail/default'

# url = 'https://72.137.146.94:8443/recapi?filedir=monitor&filename=auto-1584218910-9058726874-6400.wav'
# url = 'https://72.137.146.94:8443/recapi?filedir=voicemail/default&filename=unavail.gsm'

# url = 'https://72.137.146.94:8443/recapi'
response = requests.get(url, auth=HTTPDigestAuth(username,password) ,verify=False)
# res = json.loads(response.content)
# print(res)
# print(response.text)
print(response)
# print(response.content)
# file = open("resp_text.txt", "w")
# file.write(response.text)

# file.close()
# import wave
# obj = wave.open(response.text,'r')
# print( "Number of channels",obj.getnchannels())
# print ( "Sample width",obj.getsampwidth())
# print ( "Frame rate.",obj.getframerate())
# print ("Number of frames",obj.getnframes())
# print ( "parameters:",obj.getparams())
# obj.close()
# file = open("resp_content.csv", "wb")
# file.write(response.content)
# file.close()

# import csv
# import wave
# 2020-03/auto-1584453545-1002-4167256167.wav@
# with open('resp_content.csv', mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         if '.wav' in row["Filename"]:
#             print(f'\t{row["Directory"]} has the {row["Filename"]} file.')
#             url = 'https://72.137.146.94:8443/recapi?filedir=monitor&filename={}'.format(row["Filename"])
#             response = requests.get(url, auth=HTTPDigestAuth(username,password) ,verify=False)
#             file = open(row["Filename"], "wb")
#             file.write(response.content)
#             file.close()
#             line_count += 1
#     print(f'Processed {line_count} lines.')
