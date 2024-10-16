import allure
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


@allure.title("Тест оформления заказа")
@allure.description("Тест проверяет возможность авторизации, добавления товаров в корзину и оформления заказа на сайте Saucedemo.")
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_order_submission(driver):
    with allure.step("Открыть сайт Saucedemo"):
        driver.get("https://www.saucedemo.com/")

    with allure.step("Войти под стандартным пользователем"):
        store_page = StorePage(driver)
        store_page.login("standard_user", "secret_sauce")

    with allure.step("Добавить товары в корзину"):
        items_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]
        store_page.add_items_to_cart(items_to_add)

    with allure.step("Перейти в корзину"):
        store_page.go_to_cart()

    with allure.step("Нажать кнопку Checkout"):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()

    with allure.step("Заполнить форму с данными пользователя"):
        first_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        last_name_input = driver.find_element(By.ID, "last-name")
        postal_code_input = driver.find_element(By.ID, "postal-code")

        first_name_input.send_keys("Денис")
        last_name_input.send_keys("Ломакин")
        postal_code_input.send_keys("117546")

    with allure.step("Продолжить оформление заказа"):
        driver.find_element(By.ID, "continue").click()

    with allure.step("Проверить общую сумму заказа"):
        total_text = store_page.get_total()
        assert total_text == "Total: $58.29", f"Ожидалось $58.29, но получено {total_text}"
