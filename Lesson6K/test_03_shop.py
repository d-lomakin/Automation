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


driver.get("https://www.saucedemo.com/")


username_input = driver.find_element(By.ID, "user-name")
password_input = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username_input.send_keys("standard_user")
password_input.send_keys("secret_sauce")
login_button.click()


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
)


items_to_add = [
    "Sauce Labs Backpack",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Onesie"
]

for item in items_to_add:

    xpath_add_to_cart = f"//div[text()='{item}']/ancestor::div[@class='inventory_item']//button"
    driver.find_element(By.XPATH, xpath_add_to_cart).click()


driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


driver.find_element(By.ID, "checkout").click()


first_name_input = driver.find_element(By.ID, "first-name")
last_name_input = driver.find_element(By.ID, "last-name")
postal_code_input = driver.find_element(By.ID, "postal-code")

first_name_input.send_keys("Денис")
last_name_input.send_keys("Ломакин")
postal_code_input.send_keys("117546")


driver.find_element(By.ID, "continue").click()


total_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
)

total_text = total_element.text
print(f"Итоговая сумма: {total_text}")


driver.quit()


assert total_text == "Total: $58.29", f"Ожидалось $58.29, но получено {total_text}"
