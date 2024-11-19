import time
from data.urls import Urls
from pages.download_page import DownloadPage


class TestDownload:
    url = Urls()

    def test_download(self, driver):
        page = DownloadPage(driver, f"{self.url.herokuapp_base_url}download")
        page.open()
        page.download_file()
        time.sleep(5)