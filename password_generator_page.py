import time
from selenium.webdriver.common.by import By

class PasswordGeneratorPage:
    # Locators
    TOGGLE_1 = "(//button[@role='switch' and @aria-checked])[1]"
    TOGGLE_2 = "(//button[@role='switch' and @aria-checked])[2]"
    TOGGLE_3 = "(//button[@role='switch' and @aria-checked])[3]"
    GENERATE_BUTTON = "//button[contains(text(), 'Generate')]"
    PASSWORD_FIELD = "//code[@class='font-mono text-xl text-white flex-1 overflow-x-auto']"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://genpass.lovable.app/")
        self.driver.maximize_window()
        time.sleep(2)

    def get_toggle_states(self):
        toggle1 = self.driver.find_element(By.XPATH, self.TOGGLE_1)
        toggle2 = self.driver.find_element(By.XPATH, self.TOGGLE_2)
        toggle3 = self.driver.find_element(By.XPATH, self.TOGGLE_3)
        return (
            toggle1,
            toggle2,
            toggle3,
            toggle1.get_attribute("aria-checked"),
            toggle2.get_attribute("aria-checked"),
            toggle3.get_attribute("aria-checked"),
        )

    def set_toggles(self, mode):
        toggle1, toggle2, toggle3, state1, state2, state3 = self.get_toggle_states()
        print(f"Initial states → Toggle1={state1}, Toggle2={state2}, Toggle3={state3}")

        if mode == "case1":
            if state1 == "false": toggle1.click()
            if state2 == "false": toggle2.click()
            if state3 == "true": toggle3.click()

        elif mode == "case2":
            if state1 == "true": toggle1.click()
            if state2 == "true": toggle2.click()
            if state3 == "false": toggle3.click()

        print(f"✅ Toggles adjusted for {mode}")
        time.sleep(1)

    def click_generate(self):
        self.driver.find_element(By.XPATH, self.GENERATE_BUTTON).click()
        time.sleep(2)

    def get_generated_password(self):
        return self.driver.find_element(By.XPATH, self.PASSWORD_FIELD).text

    def validate_password(self, password, mode):
        has_upper = any(ch.isupper() for ch in password)
        has_lower = any(ch.islower() for ch in password)
        has_digit = any(ch.isdigit() for ch in password)

        if mode == "case1":
            if has_upper and has_lower:
                print(f"✅ Case1: Perfect password → {password}")
            elif has_upper and has_digit:
                raise AssertionError(f"❌ Case1: Not working → {password}")

        elif mode == "case2":
            if has_digit:
                print(f"✅ Case2: Strong password (upper + digit) → {password}")
            else:
                raise AssertionError(f"❌ Case2: Not working → {password}")








