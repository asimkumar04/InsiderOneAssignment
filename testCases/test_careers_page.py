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
        driver.get("https://insiderone.com/careers/quality-assurance/")
        driver.maximize_window()
        driver.find_element(By.XPATH,careers_page.ccokie_btn_xpath).click()
        time.sleep(2)

        all_qa_jobs_btn = driver.find_element(By.XPATH,careers_page.all_qa_job_btn_xpath)
        all_qa_jobs_btn.is_displayed()
        all_qa_jobs_btn.click()
        time.sleep(2)

        location = Select(driver.find_element(By.ID, "filter-by-location"))
        location.select_by_visible_text("Istanbul")

        department = Select(driver.find_element(By.ID, careers_page.filter_by_department_id))
        department.select_by_visible_text("Quality Assurance")
        time.sleep(2)

        result_card = driver.find_elements(By.XPATH,careers_page.result_card_xpath)
        for result in result_card:
            location = result.find_element(By.TAG_NAME, "div")
            dep = result.find_element(By.TAG_NAME,"span")
            if location.text == "Istanbul" and dep.text == "Quality Assurance":
                assert True
            else:
                allure.attach(driver.get_screenshot_as_png(), name="failureScreenshot",
                              attachment_type=AttachmentType.PNG)
                assert False



        driver.close()


