import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.careerspage import careers_page
from testCases.conftest import driver

class TestCareersPage:
    def test_qa_opportunity_turkey(self, driver):
        career = careers_page(driver)
        career.load()
        career.click_cookie_btn()

        career.select_location("Istanbul")
        career.select_department("Quality Assurance")

        result_card = driver.find_elements(By.XPATH,careers_page.result_card_xpath)
        for result in result_card:
            location = result.find_element(By.TAG_NAME, "div")
            dep = result.find_element(By.TAG_NAME,"span")
            if location.text == "Istanbul" and dep.text == "Quality Assurance":
                assert True
            else:
                allure.attach(driver.get_screenshot_as_png(), name="testCareersPage",
                              attachment_type=AttachmentType.PNG)
                assert False



        driver.close()


