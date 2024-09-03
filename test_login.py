import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@allure.feature('Login Test')
@allure.title('Login and Error')
def test_login():
    driver = webdriver.Chrome()
    
    try:
        # Open the web application
        driver.get("https://magento.softwaretestingboard.com/")
        time.sleep(5)
        
        # Click on Sign In
        sign_in_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Sign In"))
        )
        sign_in_button.click()
        time.sleep(5)
        
        # Enter valid credentials
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        password_input = driver.find_element(By.ID, "pass")
        email_input.send_keys("hellozsjvsszj@gmail.com")
        password_input.send_keys("Shashank@2003")
        
        login_button = driver.find_element(By.ID, "send2")
        login_button.click()
        time.sleep(5)
        
        # Validate successful login
        welcome_text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Welcome,')]"))
        )
        assert "Welcome" in welcome_text.text
        allure.step('Verify correct login')

        print("Successfully logged in with correct info -> Test Pass")
        
        time.sleep(5)
        
        # Logout and test incorrect credentials
        driver.get("https://magento.softwaretestingboard.com/customer/account/logout/")
        time.sleep(5)
        
        sign_in_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Sign In"))
        )
        sign_in_button.click()
        
        email_input = driver.find_element(By.ID, "email")
        password_input = driver.find_element(By.ID, "pass")
        email_input.send_keys("shashak2020csai129@abesit.edu.in")
        password_input.send_keys("Shahank@2003")  # Incorrect password
        
        login_button = driver.find_element(By.ID, "send2")
        login_button.click()
        time.sleep(5)
        
        # Validate error message
        error_message_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "messages"))
        )
        message=error_message_element.text
        assert message in error_message_element.text
        print(error_message_element.text + " -> Test Pass")
        allure.step('Verify incorrect login')
        

    
    finally:
        driver.quit()

test_login()
