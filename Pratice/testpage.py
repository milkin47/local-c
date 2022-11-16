import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

s = Service("D:\Automation_files\chromedriver.exe")
#driver = webdriver.chrome(Service=s)
driver = webdriver.Chrome(executable_path ="D:\Automation_files\chromedriver.exe")
driver.get("https://www.redbus.in/")
time.sleep(3)
driver.maximize_window()
help_button = driver.find_element_by_xpath("//a[text()='Help']").click()
time.sleep(3)






