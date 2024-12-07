from data.urls import Urls
from pages.frame_page import FramePage


class TestFrame:
    url = Urls()

    def test_frame(self, driver):
        page = FramePage(driver, self.url.demoqa_frames_url)
        page.open()
        result1 = page.check_frame("frame1")
        result2 = page.check_frame("frame2")
        assert result1 == ['500px', '350px', 'This is a sample page'], "The frame does not exist"
        assert result2 == ['100px', '100px', 'This is a sample page'], "The frame does not exist"