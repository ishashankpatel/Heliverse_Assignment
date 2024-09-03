import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@allure.feature('UI Test')
@allure.title('UI Elements')
def test_ui():

    
    try:
        # Open the web application
        driver = webdriver.Chrome()
        driver.get("https://magento.softwaretestingboard.com/")
        time.sleep(5)
        # Validate the presence of the search bar
        search_bar = driver.find_element('id',"search")
        assert search_bar.is_displayed()

        # Validate the presence of the navigation menu
        nav_menu = driver.find_element('id',"store.menu")
        assert nav_menu.is_displayed()

        # Validate the presence of the footer
        footer = driver.find_element('xpath',".//following::footer[contains(@class, 'page-footer')]")
        assert footer.is_displayed()
        time.sleep(5)


    finally:
        driver.quit()
test_ui()