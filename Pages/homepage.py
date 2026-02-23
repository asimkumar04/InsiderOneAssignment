from selenium.webdriver.common.by import By
from Pages.basepage import BasePage

class home_page(BasePage):
    ccokie_btn_xpath = (By.XPATH, "//a[@id = 'wt-cli-accept-all-btn']")
    tour_btn_xpath = (By.XPATH, "//a[contains(text(),'Platform Tour')]")


    def load(self, base_url: str):
        self.open(base_url)

    def click_cookies(self):
        self.click(self.ccokie_btn_xpath)

    def find_tour(self):
        self.is_visible(self.tour_btn_xpath)






