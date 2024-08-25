from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

def test_login_page(driver):
    login_page = LoginPage(driver) #creating instance of LoginPage class
    login_page.load() #navigate to login page
    time.sleep(5)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(login_page.dashboard)
    )

    assert login_page.is_login_element_found_successful(), "login Page displayed"



def test_invalid_login_credentials(driver):
    login_page = LoginPage(driver)  # creating instance of LoginPage class
    login_page.load()  # navigate to login page
    time.sleep(5)
    login_page.enter_user_email("farzana@gmail.com")
    login_page.enter_user_password("43r656f8")
    login_page.click_login()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(login_page.invalid_error_text)
    )
    assert login_page.is_login_user_password_invalid(), "Invalid user or password text displayed"
    time.sleep(15)



def test_login_character_validation(driver):
    login_page = LoginPage(driver) #creating instance of LoginPage class
    login_page.load() #navigate to login page
    time.sleep(5)
    login_page.enter_user_email("farzana@gmail.com")
    login_page.enter_user_password("43rf")
    login_page.click_login()

    #print(driver.page_source)

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(login_page.invalid_char_text)
    )

    assert login_page.is_login_credentials_character_limit_not_matched(), "Password validation warning test displayed"
    time.sleep(15)








