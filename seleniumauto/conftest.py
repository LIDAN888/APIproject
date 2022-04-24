import pytest
from selenium import webdriver
driver=None
@pytest.fixture(scope="session",autouse=True)
def open_chrome():
    global driver
    if driver is None:
        driver=webdriver.Chrome()
    yield driver
    # driver.quit()

