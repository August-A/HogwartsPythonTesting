from selenium.webdriver.common.by import By

from pageobject2.page.add_member import AddMember
from pageobject2.page.base_page import BasePage


class Index(BasePage):
    def goto_add_member(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap").click()
        return AddMember(self.driver)

    def import_address(self):
        pass

    def member_join(self):
        pass
