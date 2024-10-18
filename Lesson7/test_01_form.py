import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.form_page import FormPage
import allure


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_service = Service(
        r'C:\Users\adm\.cache\selenium\chromedriver\win64\128.0.6613.119\chromedriver.exe')
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    yield driver
    driver.quit()


@allure.title("Тест на отправку формы с валидацией")
@allure.description("Тест проверяет отправку формы и правильность валидации полей, включая подсветку Zip code.")
@allure.feature("Форма регистрации")
@allure.severity(allure.severity_level.CRITICAL)
def test_form_submission(driver):
    with allure.step("Открыть страницу формы"):
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    form_page = FormPage(driver)

    form_data = {
        "first_name": "Иван",
        "last_name": "Петров",
        "address": "Ленина, 55-3",
        "zip_code": "",
        "city": "Москва",
        "country": "Россия",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "job_position": "QA",
        "company": "SkyPro"
    }

    with allure.step("Заполнить форму данными"):
        form_page.fill_form(form_data)

    with allure.step("Отправить форму"):
        form_page.submit()

    with allure.step("Проверить, что поле Zip code подсвечено красным"):
        assert form_page.check_highlight(
            "zip_code", "alert-danger"), "Zip code не подсвечен красным!"

    fields_to_check = [
        "first_name", "last_name", "address", "city", "country",
        "e-mail", "phone", "job_position", "company"
    ]
    for field in fields_to_check:
        with allure.step(f"Проверить, что поле {field.replace('-', ' ').title()} подсвечено зелёным"):
            assert form_page.check_highlight(
                field, "alert-success"), f"{field.replace('-', ' ').title()} не подсвечен зеленым!"
