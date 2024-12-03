import random

from locators.drag_and_drop_locators import DragAndDropLocators
from pages.base_page import BasePage


class DragAndDropPage(BasePage):
    locators = DragAndDropLocators()

    def drag_and_drop(self):
        source_elem = self.element_is_visible(self.locators.DRAG_ME_LOC)
        target_elem = self.element_is_visible(self.locators.DROP_ME_LOC)
        self.action_drag_and_drop(source_elem, target_elem)
        text = self.element_is_visible(self.locators.DROP_ME_TEXT_LOC).text
        return text

    def draggable(self, x, y):
        elem = self.element_is_visible(self.locators.DRAG_LOC)
        coords_before = elem.location
        self.action_drag_and_drop_by_offset(elem, x, y)
        coords_after = elem.location
        return coords_before, coords_after

    def check_coords(self, coords_before, coords_after):
        x = coords_after["x"] - coords_before["x"]
        y = coords_after["y"] - coords_before["y"]
        return x, y