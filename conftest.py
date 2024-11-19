import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from functions import get_root_path

download_path = get_root_path("data\download")

@pytest.fixture
def driver():
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default.directory": download_path
    }

    options.add_argument("--window-size=1600,1000")
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(service=service, options=options)

    yield driver
    driver.quit()