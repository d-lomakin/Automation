from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options()


chrome_service = Service(
    r'C:\Users\adm\.cache\selenium\chromedriver\win64\128.0.6613.119\chromedriver.exe')


driver = webdriver.Chrome(service=chrome_service, options=chrome_options)


driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")


delay_input = driver.find_element(By.ID, "delay")
delay_input.clear()
delay_input.send_keys("45")


driver.find_element(By.XPATH, "//span[text()='7']").click()
driver.find_element(By.XPATH, "//span[text()='+']").click()
driver.find_element(By.XPATH, "//span[text()='8']").click()
driver.find_element(By.XPATH, "//span[text()='=']").click()


result_element = WebDriverWait(driver, 50).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
)

result_text = driver.find_element(By.CSS_SELECTOR, ".screen").text.strip()
assert result_text == "15", f"Ожидалось 15, но получено '{result_text}'"


driver.quit()
