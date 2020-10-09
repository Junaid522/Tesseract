import csv
import requests
import favicon
from lxml import html

headers = {'User-agent': 'Mozilla/5.0'}


def get_data():
    response = requests.get('https://web3.ncaa.org/directory/api/directory/memberList?type=12&sportCode=MBA&_=1599570913592', stream=True, headers=headers)
    data = response.json()
    for index, d in enumerate(data):

        res = requests.get('https://web3.ncaa.org/directory/orgDetail?id=' + str(d.get('orgId')), stream=True, headers=headers)
        tree = html.fromstring(res.content)
        img = tree.xpath('//div[@class="col-sm-8 col-md-8"]//img/@src')
        address = tree.xpath('//div[@class="col-sm-8 col-md-8"]//address//span')
        elements = tree.xpath('//div[@class="col-sm-8 col-md-8"]//div//div')
        # bs = BeautifulSoup(res.content, 'lxml')
        print(img)
        print(address[-3].text, address[-2].text, address[-1].text)
        spans = elements[-2].xpath('//div[@class="col-sm-8 col-md-8"]//div//div//span')
        print(spans[-2].text, spans[-1].text)

        # print(d.get('nameOfficial'))
        # print(d.get('division'))
        # print(d.get('conferenceName'))
        # print(d.get('webSiteUrl'))
        # print(d.get('athleticWebUrl'))
        # print(d.get('memberOrgAddress').get('state'))
        # print(d.get('sportRegion'))
        # print(d.get('privateFlag'))


get_data()
