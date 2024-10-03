import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.calc_page import SlowCalculatorPage


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_service = Service(
        r'C:\Users\adm\.cache\selenium\chromedriver\win64\128.0.6613.119\chromedriver.exe')
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    calculator_page = SlowCalculatorPage(driver)

    calculator_page.set_delay("45")

    calculator_page.calculate_sum()

    result_text = calculator_page.get_result()

    assert result_text == "15", f"Ожидалось 15, но получено '{result_text}'"
