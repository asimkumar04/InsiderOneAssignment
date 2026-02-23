import os

import pytest
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options

from screenshot_utility import take_screenshot

load_dotenv()


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver
    driver.quit()
@pytest.fixture()
def base_url():
    return os.getenv("BASE_URL")

@pytest.fixture()
def credentials():
    return {
        "username" : os.getenv("USERNAME"),
        "password" : os.getenv("PASSWORD")
    }

@pytest.hookimpl(optionalhook=True, hookwrapper=True)
def pytest_run_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            take_screenshot(driver, f"FAILED_{item.name}")