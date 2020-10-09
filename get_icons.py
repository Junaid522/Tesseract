import json

import requests
import scrapy
import pandas as pd
import os


def clean_url(url):
    url = url.replace("['", "")
    url = url.replace("']", "")
    url = url.lower()
    return url


def start_requests():
    df = pd.read_csv('schools_data__completed.csv')
    urls = df['Primary URL']
    for url in urls:
        print('URL: ', url)
        scrapy.Request(url=url, callback=parse)


def parse(response):
    print("\n\n<<<< Starting >>>>")

    # List possible logo extensions
    ext_list = [".png", ".gif", ".jpg", ".tif", ".tiff", ".bmp", ".svg"]

    # Extract the Home Page Address or Website First Page Address
    str_url = str(response.url).lower()
    parts = len(str_url.split("/"))
    if len(str_url.split("/")[parts - 1]) == 0:
        homepage = str_url.split("/")[parts - 2]
    else:
        homepage = str_url.split("/")[parts - 1]
    print(homepage)

    img_url_list = []
    url_list = []
    case_list = []

    ### Case 1: when <a> contains <img> with logo substring in its @src
    CHECK = False
    for tag_a in response.xpath('//a'):
        for tag_img in tag_a.xpath('.//img'):
            img_url = str(tag_img.xpath('@src').extract())
            img_url = clean_url(img_url)
            ind = img_url.find('logo')
            if ind > 0:
                CHECK = True
                img_url_list.append(img_url)
                url_list.append(str_url)
                case_list.append('1')

    ### Case 2: when <div> contains <img>  with logo substring in its @src
    if not CHECK:
        for tag_div in response.xpath('//div'):
            for tag_img in tag_div.xpath('.//img'):
                img_url = str(tag_img.xpath('@src').extract())
                img_url = clean_url(img_url)
                ind = img_url.find('logo')
                if ind > 0:
                    CHECK = True
                    img_url_list.append(img_url)
                    url_list.append(str_url)
                    case_list.append('2')

    ### Case 3: when <a> contains @href as home page address or index. and
    # <img> with possible file extension as like (.png, .gif, .jpg etc) and logo substring in its @class or @title or @alt
    if not CHECK:
        for tag_a in response.xpath('//a'):
            a_href = str(tag_a.xpath('@href').extract())
            a_href = clean_url(a_href)
            if a_href[:6] == str("index.") or a_href == homepage:
                for tag_img in tag_a.xpath('.//img'):
                    img_url = str(tag_img.xpath('@src').extract())
                    img_url = clean_url(img_url)
                    img_name, img_ext = os.path.splitext(img_url)

                    tag_class = str(tag_img.xpath('@class').extract()).lower().strip()
                    title = str(tag_img.xpath('@title').extract()).lower().strip()
                    alt = str(tag_img.xpath('@alt').extract()).lower().strip()

                    if img_ext in ext_list or tag_class.find("logo") > 0 or title.find("logo") > 0 or \
                            alt.find("logo") > 0:
                        CHECK = True
                        img_url_list.append(img_url)
                        url_list.append(str_url)
                        case_list.append('3')

    data = {'img_url_list': img_url_list, 'url_list': url_list, 'case_list': case_list}
    df = pd.DataFrame(data)
    filename = homepage + '.csv'
    print(filename)
    df.to_csv(filename, index_col=False)

    # for div in response.css('div'):
    #     for img in div.xpath('img'):
    #         for attr in img.css('img::attr(src)'):
    #             img_url = str(attr.extract()).lower()
    #             ind = img_url.find('logo')
    #             if ind > 0:
    #                 div_list.append(str(div.extract()))
    #                 img_list.append(str(img.extract()))
    #                 img_url_list.append(str(img_url))
    #                 #print(img_url)
    print("<<<< Ending >>>>\n\n")


def test():
    print('test')
    df = pd.read_csv('schools_data__completed.csv')
    print(df)
    urls = df['Primary URL']
    print(urls)
    for url in urls:
        print('URL: ', url)
        url = 'https://{}'.format(url)
        # scrapy.Request(url=url, callback=parse)
        r = requests.get(url)
        try:
            print(json.loads(r.json()))
        except ValueError:
            print("Response content is not valid JSON")


if __name__ == "__main__":
    test()
