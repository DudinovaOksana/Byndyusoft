from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class ByndyusoftLocators:
    KNOW_MORE_BUTTON = (By.XPATH, "//section[@class='knowMore']//span")
    TG_LINK = (By.CSS_SELECTOR, ".popup-callback__footer-linkTg.ml40")


class ByndyusoftPage(BasePage):
    def scroll_to_and_click_know_more_button(self):
        know_more_button = self.find_element(ByndyusoftLocators.KNOW_MORE_BUTTON)
        actions = ActionChains(self.driver)
        actions.move_to_element(know_more_button).perform()
        know_more_button.click()


    def check_tg_link(self, expected_link):
        tg_link = self.find_element(ByndyusoftLocators.TG_LINK)
        assert tg_link.get_attribute("href") == expected_link, "Link is incorrect"
