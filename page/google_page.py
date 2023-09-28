from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class GoogleLocators:
    SEARCH_BAR = (By.XPATH, '//textarea[@type="search"]')
    FIRST_RESULT = (By.XPATH, "//div[@id='search']//a")


class GooglePage(BasePage):
    def enter_word_and_press_enter(self, word):
        search_field = self.find_element(GoogleLocators.SEARCH_BAR)
        search_field.click()
        search_field.send_keys(word)
        search_field.send_keys(Keys.ENTER)

    def click_first_result(self):
        first_result = self.find_element(GoogleLocators.FIRST_RESULT)
        first_result.click()