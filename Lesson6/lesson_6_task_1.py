from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

try:

    driver.get("http://uitestingplayground.com/ajax")

    button = driver.find_element(By.CSS_SELECTOR, "button#ajaxButton")
    button.click()

    WebDriverWait(driver, 16).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div#content > p"))
    )

    result = driver.find_element(By.CSS_SELECTOR, "div#content > p").text

    print(result)

finally:

    driver.quit()
