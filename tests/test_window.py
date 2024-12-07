from data.urls import Urls
from pages.browser_window_page import BrowserWindowPage


class TestWindowPage:
    url = Urls()

    def test_window_new_tab(self, driver):
        page = BrowserWindowPage(driver, self.url.demoqa_window_url)
        page.open()
        text_result = page.check_opened_new_tab()
        assert text_result == "This is a sample page", "New tab is not found"

    def test_window_new_window(self, driver):
        page = BrowserWindowPage(driver, self.url.demoqa_window_url)
        page.open()
        text_result = page.check_opened_new_window()
        assert text_result == "This is a sample page", "New window is not found"