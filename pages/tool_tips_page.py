from locators.tool_tips_page_locators import ToolTipsPageLocators
from pages.base_page import BasePage


class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators()

    def hover_btn(self):
        elem = self.element_is_visible(self.locators.TOOL_TIPS_BTN_LOC)
        self.action_move_to_element(elem)


    def get_text(self):
        text = self.element_is_visible(self.locators.HOVER_MSG_LOC).text
        return text

    def get_css_property(self, property_name):
        data = self.element_is_visible(self.locators.TOOL_TIPS_BTN_LOC)
        return data.value_of_css_property(property_name)