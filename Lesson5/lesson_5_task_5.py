from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(
    r'C:\Users\adm\.cache\selenium\chromedriver\win64\128.0.6613.119\chromedriver.exe')


driver = webdriver.Chrome(service=service)

try:

    driver.get("https://www.python.org/")

    donate_button = driver.find_element(By.LINK_TEXT, "Donate")
    donate_button.click()

finally:

    driver.quit()
