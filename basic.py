from selenium import webdriver

from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys

service_obj = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)
driver.maximize_window()
driver.get("https://www.udemy.com/course/learn-selenium-automation-in-easy-python-language/")
print(driver.current_url)
print(driver.title)
# open in a new tab
driver.execute_script("window.open('https://github.com/','new window')")

#close current browser
driver.quit()

#close all browser
driver.close()
