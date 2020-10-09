from bs4 import BeautifulSoup
from selenium import webdriver
from seleniumwire import webdriver  # Import from seleniumwire
from time import sleep
import requests
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# proxy = {'address': '91.189.238.66:8081',
#          'username': 'offensa2',
#          'password': 'QQV7PLKB'}
#
# capabilities = dict(DesiredCapabilities.CHROME)
# capabilities['proxy'] = {'proxyType': 'MANUAL',
#                          'httpProxy': proxy['address'],
#                          'ftpProxy': proxy['address'],
#                          'sslProxy': proxy['address'],
#                          'noProxy': '',
#                          'class': "org.openqa.selenium.Proxy",
#                          'autodetect': False}

# capabilities['proxy']['socksUsername'] = proxy['username']
# capabilities['proxy']['socksPassword'] = proxy['password']

# safari = webdriver.Safari(desired_capabilities=capabilities)
# firefox_options.add_argument('--proxy-server=%s' % proxy)
PROXY = "104.139.71.127:58366"
# browser = webdriver.Chrome('./chromedriver')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)
# chrome = webdriver.Chrome(firefox_options=firefox_options)
chrome = webdriver.Chrome('./chromedriver')
# webdriver.Fire
chrome.get("https://public.tableau.com/views/Membership-tableau-combinedMaps-v4/DB-V3?%3Aembed=y&%3AshowVizHome=no&%3Ahost_url=https%3A%2F%2Fpublic.tableau.com%2F&%3Aembed_code_version=3&%3Atabs=no&%3Atoolbar=yes&%3Aanimate_transition=yes&%3Adisplay_static_image=no&%3Adisplay_spinner=no&%3Adisplay_overlay=yes&%3Adisplay_count=yes&%3AloadOrderID=0")
sleep(10)

request = chrome.wait_for_request('https://public.tableau.com/vizql/w/Membership-tableau-combinedMaps-v4/v/DB-V3/sessions/F19F1820B06C4A3B94DF3F2AEEBFC202-0:0/commands/tabsrv/render-tooltip-server', timeout=30)
# Access requests via the `requests` attribute
for request in chrome.requests:
    if request.response:
        print(
            request.url,
            request.response.status_code,
            request.response.headers['Content-Type'],
            'REQUEST RESPONSE HHH: ',request.response
        )


# from selenium.webdriver.common.action_chains import ActionChains

# hov = ActionChains(chrome)
# parent_level_menu = chrome.find_element_by_class_name("tabCanvas")
# hov.move_to_element(parent_level_menu).perform()

# print(hov)
# print(chrome.executeScript( "return window.performance.getEntriesByType('resource');" ))
# chrome.get(
#     "https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=718162-B21&rh=i%3Aaps%2Ck%3A718162-B21")
# sleep(30)
# chrome.get("https://www.racingpost.com//profile/horse/1485764/paramount-love/pedigree#race-id=714475")
# sleep(1)
# chrome.get_network_conditions()
# soup = BeautifulSoup(chrome.page_source, "lxml")

# login_button_xpath = '//*[@id="tblVerticalMode"]/tbody/tr[9]/td/div/div'
# login_button = chrome.find_element_by_xpath(login_button_xpath)
# login_button.click()
# cookies_list = chrome.get_cookies()
# cookies_dict = {}
# for cookie in cookies_list:
#     if cookie['name'] == "ak_bmsc" or cookie['name'] == "akavpau_VP1" \
#             or cookie['name'] == "_ga":
#         cookies_dict[cookie['name']] = cookie['value']
# print(cookies_dict)
# sleep(1)
# print(soup.prettify())
# all_ps = soup.find_all("p", attrs={'class': "XzvDs _208Ie _1y8M6 _2p1aK"})
# print(all_ps)
# with open("bombx.txt", "w") as ops:
#     for ps in all_ps:
#         ops.write(ps.text + "\n")
# sleep(40)
#
# sleep(40)
chrome.close()
