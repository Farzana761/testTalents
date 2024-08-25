from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

import time


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://testtalents.com/auth/login"
        self.user_email_input = (By.XPATH, "//*[@id='recruiterLoginEmail']")
        self.user_password_input = (By.XPATH, "//*[@id='recruiterLoginPassword']")
        self.login_button = (By.XPATH, "//button[@id='recruiterLoginFormButton']")
        self.dashboard = (By.XPATH, "//h1[contains(text(),'Login')]")
        self.invalid_error_text = (By.XPATH, "//div[contains(text(),'Invalid username or password')]")
        self.invalid_char_text = (By.XPATH, "//div[contains(text(),'Password should be of at least 8 characters.')]")

    def load(self):
        self.driver.get(self.url)

    def enter_user_email(self, useremail):
        self.driver.find_element(*self.user_email_input).send_keys(useremail)

    def enter_user_password(self,userpassword):
        self.driver.find_element(*self.user_password_input).send_keys(userpassword)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()



    # def is_login_successful(self):
    #     try:
    #         # Assuming 'self.dashboard' is a locator for the dashboard element
    #         dashboard_element = self.driver.find_element(*self.dashboard)
    #         return dashboard_element.is_displayed()
    #     except NoSuchElementException:
    #         return False

    def is_login_element_found_successful(self):
        try:
            dashboard_element = self.driver.find_element(*self.dashboard)
            if dashboard_element.is_displayed():
                print("Login text displayed.")
                return True
            else:
                print("login text is not displayed.")
                return False
        except NoSuchElementException:
            print("Login element was not found.")
            return False

    def is_login_user_password_invalid(self):
        try:
            error_element = self.driver.find_element(*self.invalid_error_text)
            if error_element.is_displayed():
                print("error text displayed.")
                return True
            else:
                print("error text is not displayed.")
                return False
        except NoSuchElementException:
            print("error element was not found.")
            return False


    def is_login_credentials_character_limit_not_matched(self):
        try:
            error_char_element = self.driver.find_element(*self.invalid_char_text)
            if error_char_element.is_displayed():
                print("error text displayed.")
                return True
            else:
                print("error text is not displayed.")
                return False
        except NoSuchElementException:
            print("error element was not found.")
            return False