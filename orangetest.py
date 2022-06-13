import os
import time
from selenium import webdriver

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox(executable_path=r'C:\Users\Administrator\Desktop\selenium\geckodriver.exe')

driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/validateCredentials")
driver.find_element_by_xpath('//*[@id="txtUsername"]').clear()
driver.find_element_by_xpath('//*[@id="txtUsername"]').send_keys('Admin')
driver.find_element_by_xpath('//*[@id="txtPassword"]').clear()
driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys('admin123')
driver.find_element_by_xpath('//*[@id="btnLogin"]').submit()
time.sleep(3)
dashboard=driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/h1').is_displayed()
if (dashboard==True):
    print('dashboard displayed')
print(driver.title)