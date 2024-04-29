from selenium.webdriver.support.ui import WebDriverWait
from test_project.service.constants import TIMEOUT


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.wait = WebDriverWait(self.browser, TIMEOUT, poll_frequency=1)

    def find_element(self, locator_type, locator):

        return self.browser.find_element(locator_type, locator)

    def find_elements(self, locator_type, locator):

        return self.browser.find_elements(locator_type, locator)
