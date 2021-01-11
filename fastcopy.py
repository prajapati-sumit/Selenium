from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

web = webdriver.Chrome()

web.get('http://timesink.be/speedy/')
code=web.find_element_by_id('rndstring')
code=code.text
inp=web.find_element_by_id('inputfield')
inp.send_keys(code)
inp.send_keys(Keys.RETURN)
