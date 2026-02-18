import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from Pages.homepage import home_page
from testCases.conftest import driver

# Verify home page load
class TestHomePage:
    def test_valid_login(self, driver):
        home = home_page(driver)
        home.load()
        home.click_cookies()
        home.find_tour()

        # Page load Validation
        actual_title = driver.title
        print("title:")
        print(actual_title)
        expected_title = "Insider One | #1 Platform for AI-Powered Customer Engagement"
        if actual_title == expected_title:
            assert True
            driver.close()
        else:
            allure.attach(driver.get_screenshot_as_png(), name="failureScreenshot",
                          attachment_type=AttachmentType.PNG)
            driver.close()
            assert False

