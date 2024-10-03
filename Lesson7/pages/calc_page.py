from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.seven_button = (By.XPATH, "//span[text()='7']")
        self.plus_button = (By.XPATH, "//span[text()='+']")
        self.eight_button = (By.XPATH, "//span[text()='8']")
        self.equals_button = (By.XPATH, "//span[text()='=']")
        self.result_display = (By.CSS_SELECTOR, ".screen")

    def set_delay(self, delay):
        delay_input_element = self.driver.find_element(*self.delay_input)
        delay_input_element.clear()
        delay_input_element.send_keys(delay)

    def calculate_sum(self):
        self.driver.find_element(*self.seven_button).click()
        self.driver.find_element(*self.plus_button).click()
        self.driver.find_element(*self.eight_button).click()
        self.driver.find_element(*self.equals_button).click()

    def get_result(self):
        WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element(self.result_display, "15")
        )
        return self.driver.find_element(*self.result_display).text.strip()
