import pytest
from selenium import webdriver

from test_project.service.constants import SBIS_LINK


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.get(SBIS_LINK)
    yield browser
    browser.quit()
