from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

try:

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    award_image = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "award"))
    )

    src_value = award_image.get_attribute("src")

    print("Значение атрибута src у картинки 'award':", src_value)


finally:

    driver.quit()
