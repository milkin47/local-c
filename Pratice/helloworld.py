import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


s = Service("D:\Automation files\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
time.sleep(4)
driver.close()
driver.quit()







