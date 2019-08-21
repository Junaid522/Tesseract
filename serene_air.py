from bs4 import BeautifulSoup
from selenium import webdriver
import time

base_url = 'https://www.sereneair.com'
browser = webdriver.Chrome('./chromedriver')
browser.get("https://sereneair.booksecure.net/criteriamini.aspx")
bs = BeautifulSoup(browser.page_source, 'html.parser')
print(bs.prettify())
time.sleep(2)
select_radio_button = browser.find_element_by_xpath(".//input[@type='radio' and @value='rOneWay2']")
select_radio_button.click()
flying_from = browser.find_elements_by_xpath(".//select[@name='ctlAvailCriteriaCustom$cboOrigin2']")
flying_to = browser.find_elements_by_xpath(".//select[@name='ctlAvailCriteriaCustom$cboDest2']")
departure = flying_from[0].find_element_by_xpath(".//option[text()='Karachi, Pakistan']")
departure.click()
destination = flying_to[0].find_element_by_xpath(".//option[text()='Lahore, Pakistan']")
destination.click()

depart_day = browser.find_elements_by_xpath(".//select[@name='ctlAvailCriteriaCustom$cboDepDay2']")
dep_day = depart_day[0].find_element_by_xpath(".//option[text()='01']")
dep_day.click()
depart_month_year = browser.find_elements_by_xpath(".//select[@name='ctlAvailCriteriaCustom$cboDepMon2']")
dep_month = depart_month_year[0].find_element_by_xpath(".//option[text()='Sep 2019']")
dep_month.click()
# return_day = browser.find_elements_by_xpath(".//select[@name='ctlAvailCriteriaCustom$cboRetDay2']")
# ret_day = return_day[0].find_element_by_xpath(".//option[text()='20']")
# ret_day.click()
# return_month_year = browser.find_elements_by_xpath(".//select[@name='ctlAvailCriteriaCustom$cboRetMon2']")
# ret_month = return_month_year[0].find_element_by_xpath(".//option[text()='Oct 2019']")
# ret_month.click()

search_button = browser.find_element_by_xpath(".//div[@class='RoundButtonRaised-MiniCriteria']")
search_button.click()
time.sleep(10)

print('logged in successfully!!')
browser.close()