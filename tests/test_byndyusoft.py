from page.byndyusoft_page import ByndyusoftPage
from page.google_page import GooglePage


class TestByndyusoft:

    def test_byndyusoft(self, driver):
        google_page = GooglePage(driver, 'https://www.google.com')
        google_page.go_to_site()
        google_page.enter_word_and_press_enter("Byndyusoft")
        google_page.click_first_result()
        byndyusoft_page = ByndyusoftPage(driver)
        byndyusoft_page.scroll_to_and_click_know_more_button()
        byndyusoft_page.check_tg_link("http://t.me/alexanderbyndyu")

