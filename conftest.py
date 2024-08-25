import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    # Set up ChromeDriver using ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()
    yield driver  # This allows the test to use the driver
    driver.quit()

