import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def open_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1080
    browser.config.window_height = 720
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options

    yield

    browser.quit()
