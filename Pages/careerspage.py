from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.basepage import BasePage


class careers_page(BasePage):
    all_qa_job_btn_xpath = (By.XPATH, "//a[text() = 'See all QA jobs']")
    ccokie_btn_xpath = (By.XPATH,"//a[@id = 'wt-cli-accept-all-btn']")
    filter_by_location_id = (By.ID,"filter-by-location")
    filter_by_department_id = (By.ID,"filter-by-department")
    result_card_xpath = "//div[@class='position-list-item-wrapper bg-light']"
    result_card_departemnt = (By.XPATH,"//div[@class='position-list-item-wrapper bg-light']/span")
    result_card_location = (By.XPATH,"//div[@class='position-list-item-wrapper bg-light']/div")
    view_role_btn_xpath = (By.XPATH,"//a[contains(text(),'View Role')]")

    def load(self):
        self.open("https://insiderone.com/careers/quality-assurance/")

    def click_cookie_btn(self):
        self.click(self.ccokie_btn_xpath)

    def all_qa_job_btn(self):
        self.is_visible(self.all_qa_job_btn_xpath)
        self.click(self.all_qa_job_btn_xpath)

    def select_location(self, location: str):
        drop = (self.find(self.filter_by_location_id))
        select = Select(drop)
        select.select_by_visible_text(location)

    def select_department(self, department: str):
        drop2 = self.find(self.filter_by_department_id)
        select = Select(drop2)
        select.select_by_visible_text(department)








