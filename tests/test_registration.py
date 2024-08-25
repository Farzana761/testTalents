# from pages.registration_page import RegistrationPage
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import pytest
#
# def test_registration_page(driver):
#     registration_page = RegistrationPage(driver)
#     registration_page.load() #navigate to reg page
#     time.sleep(15)
#
#     WebDriverWait(driver, 28).until(
#         EC.presence_of_element_located(registration_page.register_dashboard)
#     )
#
#     assert registration_page.is_register_element_found_successful(), "Registration Page displayed"
#     time.sleep(15)


from pages.registration_page import RegistrationPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import pytest


def test_registration_page(driver):
    registration_page = RegistrationPage(driver)

    # Load the login page
    registration_page.load()

    # Wait for and click the "Create an Account" button to navigate to the registration page
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(registration_page.create_account_button)
        ).click()
        print("Clicked on Create an Account button.")
    except TimeoutException:
        print("TimeoutException: Create an Account button was not clickable.")
        #print(driver.page_source)  # Print the page source for debugging
        #driver.save_screenshot('create_account_button_issue.png')  # Take a screenshot for debugging
        raise

    # Wait for the registration dashboard to be present on the registration page
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(registration_page.register_dashboard)
        )
        print("Registration dashboard element is present.")
    except TimeoutException:
        print("TimeoutException: The registration dashboard element was not found.")
        #print(driver.page_source)  # Print the page source for debugging
        #driver.save_screenshot('registration_page_issue.png')  # Take a screenshot for debugging
        raise

    # Verify that the registration dashboard element is displayed
    assert registration_page.is_register_element_found_successful(), "Registration Page displayed"
    time.sleep(15)

def test_fullname_empty(driver):
    registration_page = RegistrationPage(driver)

    # Load the login page
    registration_page.load()
    time.sleep(5)

    # Navigate to the registration page
    registration_page.click_on_create_account_link()

    # Wait for the registration dashboard to be present
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(registration_page.register_dashboard)
        )
        print("Registration dashboard element is present.")
    except TimeoutException:
        print("TimeoutException: Registration dashboard element was not found.")
        #print(driver.page_source)  # Print the page source for debugging
        #driver.save_screenshot('registration_page_issue.png')  # Take a screenshot for debugging
        raise

    # Enter details on the registration page
    registration_page.enter_full_name("")
    registration_page.enter_business_email("farzanaaktar761@gmail.com")
    registration_page.enter_password("1qazZAQ!")
    registration_page.enter_confirm_password("1qazZAQ!")
    registration_page.click_sign_up()

    # Wait for the error message indicating full name is empty
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(registration_page.fullname_empty_error)
        )
        print("Full name error message is displayed.")
    except TimeoutException:
        print("TimeoutException: Full name error message was not found.")
        #print(driver.page_source)  # Print the page source for debugging
        #driver.save_screenshot('fullname_error_message_issue.png')  # Take a screenshot for debugging
        raise

    # Verify the error message is displayed
    assert registration_page.is_fullname_is_empty(), "Expected error message for empty full name field is not displayed."



def test_email_invalid(driver):
    registration_page = RegistrationPage(driver)

    # Load the login page
    registration_page.load()
    time.sleep(5)

    # Navigate to the registration page
    registration_page.click_on_create_account_link()

    # Wait for the registration dashboard to be present
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(registration_page.register_dashboard)
        )
        print("Registration dashboard element is present.")
    except TimeoutException:
        print("TimeoutException: Registration dashboard element was not found.")
        #print(driver.page_source)  # Print the page source for debugging
        #driver.save_screenshot('registration_page_issue.png')  # Take a screenshot for debugging
        raise

    # Enter details on the registration page
    registration_page.enter_full_name("farzana lubna")
    registration_page.enter_business_email("farzanaaktar761.@l.com")
    registration_page.enter_password("1qazZAQ!")
    registration_page.enter_confirm_password("1qazZAQ!")
    registration_page.click_sign_up()

    # Wait for the error message indicating email is invalid
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(registration_page.business_email_invalid)
        )
        print("email error message is displayed.")
    except TimeoutException:
        print("TimeoutException: email error message was not found.")
        #print(driver.page_source)  # Print the page source for debugging
        #driver.save_screenshot('email_error_message_issue.png')  # Take a screenshot for debugging
        raise

    # Verify the error message is displayed
    assert registration_page.is_email_is_invalid(), "Expected error message for empty email field is  displayed."
    time.sleep(15)

def test_password_mismatch_error_check(driver):
    registration_page = RegistrationPage(driver)

    # Load the login page
    registration_page.load()
    time.sleep(5)

    # Navigate to the registration page
    registration_page.click_on_create_account_link()

    # Wait for the registration dashboard to be present
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(registration_page.register_dashboard)
        )
        print("Registration dashboard element is present.")
    except TimeoutException:
        print("TimeoutException: Registration dashboard element was not found.")
        #print(driver.page_source)  # Print the page source for debugging
        #driver.save_screenshot('registration_page_issue.png')  # Take a screenshot for debugging
        raise

    # Enter details on the registration page
    registration_page.enter_full_name("farzana lubna")
    registration_page.enter_business_email("farzanaaktar761@gmail.com")
    registration_page.enter_password("1qazZAQ!")
    registration_page.enter_confirm_password("1qazZA!")
    registration_page.click_sign_up()

    # Wait for the error message indicating email is invalid
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(registration_page.password_mismatch_error)
        )
        print("password error message is displayed.")
    except TimeoutException:
        print("TimeoutException: password error message was not found.")
        #print(driver.page_source)  # Print the page source for debugging
        #driver.save_screenshot('password_error_message_issue.png')  # Take a screenshot for debugging
        raise

    # Verify the error message is displayed
    assert registration_page.is_password_matched(), "Expected error message for mismatch password is  displayed."
    time.sleep(15)