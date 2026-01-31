import time
from selenium import webdriver
from password_generator_page import PasswordGeneratorPage

def run_test_case(driver, mode):
    print(f"\n==============================")
    print(f"🔹 Running {mode}")
    print(f"==============================")

    page = PasswordGeneratorPage(driver)
    page.set_toggles(mode)
    page.click_generate()

    
    password = page.get_generated_password()
    print(f"Generated Password ({mode}): {password}")

    page.validate_password(password, mode)
    time.sleep(1)


# Main test flow
driver = webdriver.Chrome()
page = PasswordGeneratorPage(driver)
page.open()

# Run both test cases
run_test_case(driver, "case1")
time.sleep(2)
driver.refresh()
time.sleep(2)
run_test_case(driver, "case2")

print("\n🎉 All test cases executed successfully!")
driver.quit()



