"""
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from password_generator_page import PasswordGeneratorPage

def test_password_generation():
    driver = webdriver.Chrome()
    driver.maximize_window()

    page = PasswordGeneratorPage(driver)
    page.open()

    # Step 1: Toggle the options
    page.toggle_options()

    # Step 2: Generate password
    page.click_generate()

    # Step 3: Validate password
    password = page.get_password_text()
    page.validate_password_strength(password)

    print(f"✅ Test Passed. Password generated: {password}")


    driver.quit()

"""
import time
from selenium import webdriver
from password_generator_page import PasswordGeneratorPage

def test_password_generation(mode="case1"):
    driver = webdriver.Chrome()
    page = PasswordGeneratorPage(driver)

    page.open()
    page.set_toggle_states(mode)
    page.click_generate()

    password = page.get_password_text()
    print(f"Generated password: {password}")

    page.validate_password_strength(password, mode)
    print(f"✅ Test completed successfully for {mode}")

    time.sleep(2)
    driver.quit()



def test_password_generation(mode="case2"):
    driver = webdriver.Chrome()
    page = PasswordGeneratorPage(driver)

    page.open()
    page.set_toggle_states(mode)
    page.click_generate()

    password = page.get_password_text()
    print(f"Generated password: {password}")

    page.validate_password_strength(password, mode)
    print(f"✅ Test completed successfully for {mode}")

    time.sleep(2)
    driver.quit()
# 🔹 Run either of these:
# test_password_generation("case1")
# test_password_generation("case2")

if __name__ == "__main__":
    #test_password_generation("case1")
    test_password_generation("case2")
