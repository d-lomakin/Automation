import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.store_page import StorePage


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_service = Service(
        r'C:\Users\adm\.cache\selenium\chromedriver\win64\128.0.6613.119\chromedriver.exe')
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    yield driver
    driver.quit()


def test_order_submission(driver):
    driver.get("https://www.saucedemo.com/")

    store_page = StorePage(driver)
    store_page.login("standard_user", "secret_sauce")

    items_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]
    store_page.add_items_to_cart(items_to_add)
    store_page.go_to_cart()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    ).click()

    first_name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )
    last_name_input = driver.find_element(By.ID, "last-name")
    postal_code_input = driver.find_element(By.ID, "postal-code")

    first_name_input.send_keys("Денис")
    last_name_input.send_keys("Ломакин")
    postal_code_input.send_keys("117546")

    driver.find_element(By.ID, "continue").click()

    total_text = store_page.get_total()

    assert total_text == "Total: $58.29", f"Ожидалось $58.29, но получено {total_text}"
