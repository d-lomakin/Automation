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

try:

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "zip-code").clear()
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    submit_button = driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    WebDriverWait(
        driver, 30).until(
        EC.presence_of_element_located(
            (By.ID, "zip-code")))

    zip_code_element = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_code_element.get_attribute(
        "class"), "Zip code is not highlighted in red!"

    fields_to_check = [
        "first-name",
        "last-name",
        "address",
        "city",
        "country",
        "e-mail",
        "phone",
        "job-position",
        "company"]
    for field in fields_to_check:
        element = driver.find_element(By.ID, field)
        assert "alert-success" in element.get_attribute(
            "class"), f"{field.replace('-', ' ').title()} is not highlighted in green!"


finally:
    driver.quit()
