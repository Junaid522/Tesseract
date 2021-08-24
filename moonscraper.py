import csv
import requests
import favicon
from bs4 import BeautifulSoup
from lxml import html

headers = {'User-agent': 'Mozilla/5.0'}


def get_data():
    response = requests.get('https://www.tipranks.com/stocks/amzn/forecast', headers=headers)
    print(response.content)
    tree = html.fromstring(response.content)
    # print(tree)
    style__consensus = tree.xpath('//div[@class="client-components-stock-research-StockPageBox-style__box stock-box-mobile-border-top-override client-components-stock-research-analysts-style__consensus client-components-stock-research-style__tabbedStockBox"]')
    address = tree.xpath('//div[@class="client-components-stock-research-StockPageBox-style__box stock-box-mobile-border-top-override client-components-stock-research-analysts-style__consensus client-components-stock-research-style__tabbedStockBox"]')
    # elements = tree.xpath('//div[@class="col-sm-8 col-md-8"]//div//div')
    bs = BeautifulSoup(response.content, 'lxml')
    print(style__consensus)
    print(address)
    # print(address[-3].text, address[-2].text, address[-1].text)
    # spans = elements[-2].xpath('//div[@class="col-sm-8 col-md-8"]//div//div//span')
    # print(spans[-2].text, spans[-1].text)


get_data()
