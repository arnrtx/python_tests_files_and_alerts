from locators.frame_page_locators import FramePageLocators
from pages.base_page import BasePage

class FramePage(BasePage):
    locators = FramePageLocators()

    def check_frame(self, frame_number):
        frame = ''
        if frame_number == 'frame1':
            frame = self.element_is_present(self.locators.BIG_FRAME)
        if frame_number == 'frame2':
            frame = self.element_is_present(self.locators.SMALL_FRAME)
        width = frame.get_attribute('width')
        height = frame.get_attribute('height')
        self.driver.switch_to.frame(frame)
        text = self.element_is_present(self.locators.FRAME_PAGE).text
        self.driver.switch_to.default_content()
        return [width, height, text]