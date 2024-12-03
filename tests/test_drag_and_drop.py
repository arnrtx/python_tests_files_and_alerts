import random
import time

from data.urls import Urls
from pages.drag_and_drop_page import DragAndDropPage


class TestDragAndDrop:

    url = Urls()

    def test_drag_and_drop(self, driver):
        page = DragAndDropPage(driver, self.url.demoqa_droppable_url)
        page.open()
        text = page.drag_and_drop()
        assert text == "Dropped!"

    def test_drag_by_offset(self, driver):
        x = random.randint(50, 200)
        y = random.randint(50, 200)
        page = DragAndDropPage(driver, self.url.demoqa_draggable_url)
        page.open()
        coords_before, coords_after = page.draggable(x, y)
        x1, y1 = page.check_coords(coords_before, coords_after)
        assert x1 == x and y1 == y