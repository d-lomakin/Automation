from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service = Service(
    r'C:\Users\adm\.cache\selenium\chromedriver\win64\128.0.6613.119\chromedriver.exe')


driver = webdriver.Chrome(service=service)

try:

    driver.get("https://www.example.com")

    title = driver.title

    print("Заголовок страницы:", title)

finally:

    driver.quit()
