import time

import pytest

from Pages.homepage import home_page

# Verify home page load
class TestHomePage:
    def test_valid_login(self, driver, base_url):
        home = home_page(driver)
        home.load(base_url)
        home.click_cookies()
        home.find_tour()

        # Validating page is loaded
        actual_title = driver.title
        print("title:", actual_title)
        expected_title = "Insider One | #1 Platform for AI-Powered Customer Engagement"
        if actual_title == expected_title:
            assert True
            driver.close()
        else:
            driver.close()
            assert False

