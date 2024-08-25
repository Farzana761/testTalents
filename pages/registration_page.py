from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

import time


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.login_url = "https://testtalents.com/auth/login"
        self.create_account_button = (By.XPATH, "//a[contains(text(),'Create an Account')]")
        self.register_dashboard = (By.XPATH, "//h1[contains(text(),'Register')]")
        self.register_full_name = (By.XPATH, "//input[@id='recruiterRegisterFullName']")
        self.register_business_email = (By.XPATH, "//input[@id='recruiterRegisterEmail']")
        self.register_password = (By.XPATH, "//input[@id='recruiterRegisterPassword']")
        self.register_confirm_password = (By.XPATH, "//input[@id='recruiterRegisterConfirmPassword']")
        self.register_button = (By.XPATH, "//button[@id='recruiterRegisterFormButton']")

        self.fullname_empty_error = (By.XPATH, "//div[contains(text(),'Please enter your full name.')]")
        self.business_email_invalid = (By.XPATH, "//div[contains(text(),'Please enter a valid business email.')]")
        self.password_mismatch_error = (By.XPATH, "//div[contains(text(),'Password and confirm password should match.')]")

    def load(self):
        self.driver.get(self.login_url)

    def click_on_create_account_link(self):
        self.driver.find_element(*self.create_account_button).click()

    def is_register_element_found_successful(self):
        try:
            register_element = self.driver.find_element(*self.register_dashboard)
            if register_element.is_displayed():
                print("register text displayed.")
                return True
            else:
                print("register text is not displayed.")
                return False
        except NoSuchElementException:
            print("register element was not found.")
            return False

    def enter_full_name(self, fullname):
        self.driver.find_element(*self.register_full_name).send_keys(fullname)

    def enter_business_email(self, useremail):
        self.driver.find_element(*self.register_business_email).send_keys(useremail)

    def enter_password(self, password):
        self.driver.find_element(*self.register_password).send_keys(password)

    def enter_confirm_password(self, confirmpassword):

        self.driver.find_element(*self.register_confirm_password).send_keys(confirmpassword)

    def click_sign_up(self):
        self.driver.find_element(*self.register_button).click()


    # def is_fullname_element_found_successful(self):
    #     try:
    #         fullname_element = self.driver.find_element(*self.register_full_name)
    #         if fullname_element.is_displayed():
    #             print("full name input field displayed.")
    #             return True
    #         else:
    #             print("full name is not displayed.")
    #             return False
    #     except NoSuchElementException:
    #         print("full name element was not found.")
    #         return False

    def is_fullname_is_empty(self):
        try:
            fullname_field_empty = self.driver.find_element(*self.fullname_empty_error)
            if fullname_field_empty.is_displayed():
                print("full name input field empty.")
                return True
            else:
                print("full name is not empty.")
                return False
        except NoSuchElementException:
            print("full name element was not found.")
            return False

    def is_email_is_invalid(self):
        try:
            email_field_invalid = self.driver.find_element(*self.business_email_invalid)
            if email_field_invalid.is_displayed():
                print("email invalid.")
                return True
            else:
                print("email is not invalid.")
                return False
        except NoSuchElementException:
            print("email element was not found.")
            return False

    def is_password_matched(self):
        try:
            password_matched_check = self.driver.find_element(*self.password_mismatch_error)
            if password_matched_check.is_displayed():
                print("password not matched.")
                return True
            else:
                print("password mathced.")
                return False
        except NoSuchElementException:
            print("password error element was not found.")
            return False