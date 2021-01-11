from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random



web = webdriver.Chrome()
web.get('https://docs.google.com/forms/d/e/1FAIpQLSdWAKVBv3yWlfRNvZQ5Ct0PamxM1k_1tDt5fm0ApHqIbZZu1w/viewform')

time.sleep(3)

emailID="tinashikha123@gmail.com"
name='Tina Shikhawat'
cl='7'
school='South Point'
roll='31'

last = web.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
'/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'

last.send_keys(emailID)
last.send_keys(Keys.TAB)

last=web.switch_to_active_element()
last.send_keys(name)
last.send_keys(Keys.TAB)

last=web.switch_to_active_element()
last.send_keys(cl)
last.send_keys(Keys.TAB)

last=web.switch_to_active_element()
last.send_keys(roll)
last.send_keys(Keys.TAB)

last=web.switch_to_active_element()
last.send_keys(school)
last.send_keys(Keys.TAB)

last=web.switch_to_active_element()
for i in range(15):
   
    
    
    for j in range(random.randint(1,4)):
        last.send_keys(Keys.ARROW_RIGHT)
        last=web.switch_to_active_element()

    last.send_keys(Keys.TAB)
    last=web.switch_to_active_element()

last.click()
    