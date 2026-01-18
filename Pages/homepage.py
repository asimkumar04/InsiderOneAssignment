from selenium.webdriver.common.by import By


class home_page:
    ccokie_btn_xpath = "//a[@id = 'wt-cli-accept-all-btn']"
    tour_btn_xpath = "//a[contains(text(),'Platform Tour')]"

    def __init__(self, driver):
        self.driver = driver


