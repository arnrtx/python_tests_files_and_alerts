import time

from data.data.registration_data import RegistrationData
from data.generator.registration_generator import RegistrationGenerator
from data.urls import Urls
from pages.registration_page import RegistrationPage


class TestRegistration:
    url = Urls()
    registration_generator = RegistrationGenerator()
    registration_data = RegistrationData()

    def test_registration(self, driver):
        info = next(self.registration_generator.generate_registration_data())
        page = RegistrationPage(driver, self.url.registration_url)
        page.open()
        page.fill_form(info)
        success_message = page.get_success_message()
        assert success_message == self.registration_data.success_reg_message