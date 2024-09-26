from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.fields = {
            "first_name": (By.NAME, "first-name"),
            "last_name": (By.NAME, "last-name"),
            "address": (By.NAME, "address"),
            "zip_code": (By.NAME, "zip-code"),
            "city": (By.NAME, "city"),
            "country": (By.NAME, "country"),
            "e-mail": (By.NAME, "e-mail"),
            "phone": (By.NAME, "phone"),
            "job_position": (By.NAME, "job-position"),
            "company": (By.NAME, "company")
        }
        self.submit_button = (By.CSS_SELECTOR, "button[type='submit']")

    def fill_form(self, data):
        wait = WebDriverWait(self.driver, 20)
        for field, value in data.items():
            try:
                element = wait.until(
                    EC.visibility_of_element_located(
                        self.fields[field]))
                if field == "zip_code" and value is None:
                    element.clear()
                else:
                    element.send_keys(value)
            except TimeoutException:
                print(f"Timeout: элемент '{field}' не найден")

    def submit(self):
        wait = WebDriverWait(self.driver, 20)
        try:
            submit_button = wait.until(
                EC.element_to_be_clickable(
                    self.submit_button))
            submit_button.click()
        except TimeoutException:
            print("Timeout: кнопка отправки не найдена или не кликабельна")

    def check_highlight(self, field, expected_class):
        wait = WebDriverWait(self.driver, 20)
        field_id = field.replace("_", "-")
        try:
            print(f"Checking highlight for field: {field_id}")
            element = wait.until(
                EC.visibility_of_element_located(
                    (By.ID, field_id)))
            return expected_class in element.get_attribute("class")
        except TimeoutException:
            print(f"Timeout: элемент '{field_id}' не найден")
            return False
