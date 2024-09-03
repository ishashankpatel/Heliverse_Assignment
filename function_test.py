import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@allure.feature('Functional Test')
@allure.title('Test Product Addition and Checkout')
def test_Functional_test():
    driver = webdriver.Chrome()
    
    try:
        driver.get("https://magento.softwaretestingboard.com/")
        allure.step('Open the web application')

        sign_in_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Sign In"))
        )
        sign_in_button.click()
        allure.step('Click on Sign In button')

        email_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "email"))
        )
        password_input = driver.find_element(By.ID, "pass")
        email_input.send_keys("hellozsjvsszj@gmail.com")
        password_input.send_keys("Shashank@2003")
        login_button = driver.find_element(By.ID, "send2")
        login_button.click()
        allure.step('Enter credentials and login')
        time.sleep(2)

        search_box = driver.find_element(By.ID, "search")
        search_box.send_keys("Tee")
        search_box.send_keys(Keys.RETURN)
        allure.step('Search for a product')
        time.sleep(2)

        sizew = driver.find_element(By.ID, "option-label-size-143-item-166")
        driver.execute_script("arguments[0].scrollIntoView(true);", sizew)
        sizew.click()

        colorw = driver.find_element(By.ID, "option-label-color-93-item-50")
        driver.execute_script("arguments[0].scrollIntoView(true);", colorw)
        colorw.click()

        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.tocart.primary"))
        )
        add_to_cart_button.click()
        allure.step('Add the product to cart')
        time.sleep(5)

        add_to_cart_butto = driver.find_element(By.CSS_SELECTOR, ".showcart")
        add_to_cart_butto.click()
        time.sleep(5)

        proceed_to_checkout = driver.find_element('id','top-cart-btn-checkout')
        proceed_to_checkout.click()
        allure.step('Proceed to checkout')
        time.sleep(5)

        wait = WebDriverWait(driver, 10)
        save_in_address_book = wait.until(
            EC.element_to_be_clickable((By.XPATH, ".//following::button[contains(@class, 'action') and contains(@class, 'continue') and contains(@class, 'primary')]"))
        )
        save_in_address_book.click()
        time.sleep(10)
        
        checkou = wait.until(
            EC.element_to_be_clickable((By.XPATH, ".//following::button[contains(@class, 'action') and contains(@class, 'primary') and contains(@class, 'checkout')]"))
        )
        checkou.click()
        time.sleep(10)
        
        expected_title = "Success Page"  # Update if necessary
        actual_title = driver.title
        assert expected_title in actual_title, f"Expected title to be '{expected_title}', but got '{actual_title}'"
        allure.step('Verify the page title')

        print("Pass")

    finally:
        driver.quit()
