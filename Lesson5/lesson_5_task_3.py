from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


service = Service(
    r'C:\Users\adm\.cache\selenium\chromedriver\win64\128.0.6613.119\chromedriver.exe')


driver = webdriver.Chrome(service=service)

try:

    driver.get("http://uitestingplayground.com/classattr")

    button = driver.find_element(By.CLASS_NAME, 'btn-primary')
    button.click()

    alert = driver.switch_to.alert
    alert.accept()

    time.sleep(10)

finally:
    driver.quit()
