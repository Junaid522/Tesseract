from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

headers={'User-Agent':'PostmanRuntime/7.11.0'}

headers = {'User_Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

url = u'https://twitter.com/search?q='
query = u'hashtag'
# r = requests.get(url + query)
req = requests.get(url, headers=headers)
print(req.status_code)

soup = BeautifulSoup(req.content, 'html.parser')
print(soup)

# import requests
# from bs4 import BeautifulSoup
#
# import sys
# import json

