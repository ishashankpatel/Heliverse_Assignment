from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import allure

@allure.feature('Form Test')
@allure.title('Form Validation')
# Setup the WebDriver
def test_Form():
    driver = webdriver.Chrome()
    try:
        

        # Navigate to the form page
        driver.get("https://fluentforms.com/forms/contact-form-demo/")

        # Locate the form elements
        first_name_input = driver.find_element(By.ID, "ff_3_names_first_name_")
        last_name_input = driver.find_element(By.ID, "ff_3_names_last_name_")
        email_input = driver.find_element(By.ID, "ff_3_email")
        subject_input = driver.find_element(By.ID, "ff_3_subject")
        message_input = driver.find_element(By.ID, "ff_3_message")
        submit_button = driver.find_element(By.CSS_SELECTOR, "button.ff-btn-submit")
        time.sleep(3)

        # Test case 1: Leave required fields empty and submit
        submit_button.click()
        time.sleep(3)

        # Validate error messages
        last_name_error = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='error text-danger' and contains(text(), 'This field is required')]"))
        )
        time.sleep(3)
        email_error = driver.find_element(By.XPATH, "//div[@class='error text-danger' and contains(text(), 'This field is required')]")
        time.sleep(3)

        message_error = driver.find_element(By.XPATH, "//div[@class='error text-danger' and contains(text(), 'This field is required')]")
        time.sleep(3)

        assert last_name_error.is_displayed(), "Last Name error message is not displayed"
        assert email_error.is_displayed(), "Email error message is not displayed"
        assert message_error.is_displayed(), "Message error message is not displayed"

        # Test case 2: Fill in the form with valid data and submit
        
        first_name_input.send_keys("John") 
        time.sleep(3)
        last_name_input.send_keys("Doe")
        time.sleep(3)
        email_input.send_keys("johndoe@example.com")
        time.sleep(3)
        subject_input.send_keys("Testing Subject")
        time.sleep(3)
        message_input.send_keys("This is a test message.")
        time.sleep(3)

        # Submit the form again
        submit_button.click()
        time.sleep(4)

        # Verify that no errors are present after valid submission
        assert len(driver.find_elements(By.XPATH, "//div[@class='error text-danger']")) == 0, "There are unexpected error messages"


        print("Form validation tests passed successfully.")

    finally:
        # Clean up by closing the browser window
        driver.quit()
test_Form()
