import os

import pytest
from selenium import webdriver

from test_project.service.constants import SBIS_LINK
from test_project.service.utils import get_chrome_download_permission


upload_file_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "downloaded_plugin"))


@pytest.fixture()
def browser():
    browser = webdriver.Chrome(options=get_chrome_download_permission(upload_file_path))
    browser.get(SBIS_LINK)
    yield browser
    browser.quit()
