"""
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class PasswordGeneratorPage:
    # Locators
    TOGGLE_1 = "(//button[@role='switch' and @aria-checked])[1]"
    TOGGLE_2 = "(//button[@role='switch' and @aria-checked])[2]"
    TOGGLE_3 = "(//button[@role='switch' and @aria-checked])[3]"
    GENERATE_BUTTON = "//button[contains(text(), 'Generate')]"
    PASSWORD_FIELD = "//code[@class='font-mono text-xl text-white flex-1 overflow-x-auto']"



    def __init__(self, driver):
        self.driver = driver

    # ---- Page Actions ----
    def open(self, url="https://genpass.lovable.app/"):
        self.driver.get(url)
        time.sleep(5)

    def toggle_options(self):
        toggle1 = self.driver.find_element(By.XPATH, self.TOGGLE_1)
        toggle2 = self.driver.find_element(By.XPATH, self.TOGGLE_2)
        toggle3 = self.driver.find_element(By.XPATH, self.TOGGLE_3)

        state1 = toggle1.get_attribute("aria-checked")
        state2 = toggle2.get_attribute("aria-checked")
        state3 = toggle3.get_attribute("aria-checked")

        if state1 == "true":
            toggle1.click()
        if state2 == "true":
            toggle2.click()
        if state3 == "false":
            toggle3.click()


    def click_generate(self):
        self.driver.find_element(By.XPATH, self.GENERATE_BUTTON).click()
        time.sleep(2)

    def get_password_text(self):
        return self.driver.find_element(By.XPATH, self.PASSWORD_FIELD).text

    def validate_password_strength(self, password: str):

        #Validates password rules using assertion
        has_upper = any(ch.isupper() for ch in password)
        has_lower = any(ch.islower() for ch in password)
        has_digit = any(ch.isdigit() for ch in password)

        #assert has_upper, f"❌ Password missing uppercase: {password}"
        #assert has_lower, f"❌ Password missing lowercase: {password}"
        assert has_digit, f"❌ Password missing digit: {password}"

        return True

"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class PasswordGeneratorPage:
    # --- Locators ---
    TOGGLE_1 = "(//button[@role='switch' and @aria-checked])[1]"
    TOGGLE_2 = "(//button[@role='switch' and @aria-checked])[2]"
    TOGGLE_3 = "(//button[@role='switch' and @aria-checked])[3]"
    GENERATE_BUTTON = "//button[contains(text(), 'Generate')]"
    PASSWORD_FIELD = "//code[@class='font-mono text-xl text-white flex-1 overflow-x-auto']"

    def __init__(self, driver):
        self.driver = driver

    # --- Page actions ---
    def open(self):
        self.driver.get("https://genpass.lovable.app/")
        self.driver.maximize_window()
        time.sleep(2)

    def set_toggle_states(self, mode="case1"):
        """Handle different toggle conditions dynamically"""
        toggle1 = self.driver.find_element(By.XPATH, self.TOGGLE_1)
        toggle2 = self.driver.find_element(By.XPATH, self.TOGGLE_2)
        toggle3 = self.driver.find_element(By.XPATH, self.TOGGLE_3)

        state1 = toggle1.get_attribute("aria-checked")
        state2 = toggle2.get_attribute("aria-checked")
        state3 = toggle3.get_attribute("aria-checked")

        print(f"Initial states → Toggle1={state1}, Toggle2={state2}, Toggle3={state3}")

        # 🔹 CASE 1: Default logic
        if mode == "case1":
            if state1 == "false":
                toggle1.click()
            if state2 == "false":
                toggle2.click()
            if state3 == "true":
                toggle3.click()

        # 🔹 CASE 2: Opposite logic
        elif mode == "case2":
            if state1 == "true":
                toggle1.click()
            if state2 == "true":
                toggle2.click()
            if state3 == "false":
                toggle3.click()

        # --- Assertion for toggle behavior ---
        print(f"✅ Toggles adjusted for {mode}")

    def click_generate(self):
        """Click on the 'Generate' button"""
        button = self.driver.find_element(By.XPATH, self.GENERATE_BUTTON)
        button.click()
        time.sleep(2)

    def get_password_text(self):
        """Fetch generated password text"""
        password = self.driver.find_element(By.XPATH, self.PASSWORD_FIELD)
        return password.text

    def validate_password_strength(self, password, mode="case1"):
        """Perform different assertions based on mode"""
        has_upper = any(ch.isupper() for ch in password)
        has_lower = any(ch.islower() for ch in password)
        has_digit = any(ch.isdigit() for ch in password)

        if mode == "case1":
            if has_upper and has_lower and has_digit:
                assert True, f"✅ Case1: Perfect password: {password}"
            else:
                assert False, f"❌ Case1: Weak password: {password}"

        elif mode == "case2":

            if has_digit:
                assert has_digit, f"❌ Password missing digit: {password}"
            elif has_lower:
                assert True, f"⚠️ Case2: Normal (only lowercase): {password}"
            else:
                assert False, f"❌ Case2: Very weak password: {password}"








