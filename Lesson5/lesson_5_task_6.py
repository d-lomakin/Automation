from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


service = Service(
    r'C:\Users\adm\.cache\selenium\chromedriver\win64\128.0.6613.119\chromedriver.exe')


driver = webdriver.Chrome(service=service)

try:

    driver.get("https://www.google.com/")

    search_box = driver.find_element(By.NAME, "q")

    search_box.send_keys("Selenium")

    search_box.send_keys(Keys.RETURN)

finally:

    driver.quit()
