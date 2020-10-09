# from tbselenium.tbdriver import TorBrowserDriver
# import tbselenium.common as cm
# from os.path import dirname, join, realpath, getsize
#
# out_img = join(dirname(realpath(__file__)), "screenshot.png")
# with TorBrowserDriver("/Applications/Tor Browser.app/Contents/MacOS/firefox", tor_cfg=cm.USE_STEM) as driver:
# 	driver.load_url('https://check.torproject.org', wait_for_page_body=True)
# 	print("----"*100)
# 	driver.get_screenshot_as_file(out_img)
# 	print("----"*100)
# print("Screenshot is saved as %s (%s bytes)" % (out_img, getsize(out_img)))
#     # driver.get()


import os
import time

import requests
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver

# path to the firefox binary inside the Tor package
binary = '/Applications/Tor Browser.app/Contents/MacOS/firefox'
if os.path.exists(binary) is False:
    raise ValueError("The binary path to Tor firefox does not exist.")
firefox_binary = FirefoxBinary(binary)

browser = None


def get_browser(binary=None):
    global browser
    # only one instance of a browser opens, remove global for multiple instances
    if not browser:
        browser = webdriver.Firefox(firefox_binary=binary)
    return browser


def main():
    browser = get_browser(binary=firefox_binary)
    urls = (
        ('wayback machine check', 'https://archive.org/web/'),
    )
    for url_name, url in urls:
        print("getting", url_name, "at", url)
        browser.get(url)
        browser.find_element_by_xpath('//input[@id="wwmurl"]').send_keys('bertrodriguez-museum.org')
        browser.find_element_by_xpath('//button[@class="web_button web_text web_bottom_10"]').click()
        print(browser.page_source)
        r = requests.get(url)
        print(r.status_code)

    time.sleep(5)
    browser.close()


if __name__ == "__main__":
    main()