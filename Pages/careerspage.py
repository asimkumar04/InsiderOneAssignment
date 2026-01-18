from selenium.webdriver.common.by import By


class careers_page:
    all_qa_job_btn_xpath = "//a[text() = 'See all QA jobs']"
    ccokie_btn_xpath = "//a[@id = 'wt-cli-accept-all-btn']"
    filter_by_location_id = "filter-by-location"
    filter_by_department_id = "filter-by-department"
    result_card_xpath = "//div[@class='position-list-item-wrapper bg-light']"
    result_card_departemnt = "//div[@class='position-list-item-wrapper bg-light']/span"
    result_card_location = "//div[@class='position-list-item-wrapper bg-light']/div"
    view_role_btn_xpath = "//a[contains(text(),'View Role')]"

    def __init__(self, driver):
        self.driver = driver




