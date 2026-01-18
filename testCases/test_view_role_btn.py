import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.careerspage import careers_page
from testCases.conftest import driver

class TestViewRoleBtn:
    def test_view_role(self, driver):
        driver.get("https://insiderone.com/careers/quality-assurance/")
        driver.maximize_window()
        driver.find_element(By.XPATH,careers_page.ccokie_btn_xpath).click()
        time.sleep(2)

        all_qa_jobs_btn = driver.find_element(By.XPATH, careers_page.all_qa_job_btn_xpath)
        all_qa_jobs_btn.is_displayed()
        all_qa_jobs_btn.click()
        time.sleep(2)

        location = Select(driver.find_element(By.ID, "filter-by-location"))
        location.select_by_visible_text("Istanbul")

        department = Select(driver.find_element(By.ID, careers_page.filter_by_department_id))
        department.select_by_visible_text("Quality Assurance")
        time.sleep(2)

        driver.find_element(By.XPATH, careers_page.view_role_btn_xpath).click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])

        leverAppUrl = driver.current_url
        #print(newUrl)
        if "https://jobs.lever.co/insiderone/" in leverAppUrl:
            assert True
            # driver.close()
        else:
            allure.attach(driver.get_screenshot_as_png(), name="failureScreenshot",
                          attachment_type=AttachmentType.PNG)
            assert False

        driver.close()



