import pytest

from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

# from test_project.service.constants import SBIS_LINK, TOTAL_TIMEOUT

# driver = webdriver.Chrome(ChromeDriverManager().install())
# config.browser_name = 'chrome'
# config.base_url = 'https://google.com'
# config.app_host = SBIS_LINK
# config.timeout = TOTAL_TIMEOUT


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
