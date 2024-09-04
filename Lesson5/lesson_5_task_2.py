from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/dynamicid")

    button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Button with Dynamic ID')]")

    button.click()

    time.sleep(2)

finally:
    driver.quit()
