from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
s = Service("D:\Automation files\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.amazon.in/")
Title = driver.title
print(Title)
driver.find_element_by_class_name("nav-line-2 ").click()
driver.find_element_by_xpath("//span[text()='Sign in").click()
time.sleep(4)
driver.find_element_by_id("ap_email").send_keys("854628464547")
driver.find_element_by_xpath("//input[@id='continue']").click()
time.sleep(3)
assert driver.find_element_by_xpath("//h4[text()='Incorrect phone number']").text == "Incorrect phone number"

