import allure
from selenium.webdriver.support import expected_conditions as ec

from test_project.service.constants import (USER_REGION, KAMCHATKA_REGION,
                                            KAMCHATKA_PARTIAL_URL, USER_REGION_PARTIAL_URL,
                                            EXPECTING_TITLE, EXPECTING_URL)
from test_project.pages.base_page import BasePage
from test_project.service.locators import SbisPageLocators


class SbisPage(BasePage):
    """Класс страницы sbis.ru."""

    @allure.step('Go to contacts page on "sbis.ru".')
    def go_to_contacts_page(self):
        """Переходим на страницу с контактами."""
        self.find_element(*SbisPageLocators.LOCATOR_SBIS_CONTACTS_LINK).click()

    @allure.step('Find and open banner Tenzor, go to "tenzor.ru".')
    def find_and_open_tenzor_banner(self):
        """Переходим на страницу 'tenzor.ru' путем нажатия на баннер."""
        with allure.step('Find banner Tenzor and click.'):
            self.find_element(*SbisPageLocators.LOCATOR_SBIS_BANNER_TENZOR_LINK).click()
        self.wait.until(ec.url_contains(USER_REGION_PARTIAL_URL))

    @allure.step('Check: user region is appeared on contacts page.')
    def check_current_user_region_is_showed(self):
        """Проверяем, что появился регион текущего пользователя."""
        with allure.step('Find region name.'):
            region = self.find_element(*SbisPageLocators.LOCATOR_SBIS_REGION)
        assert USER_REGION == region.text, 'Регион пользователя не совпадает.'

    @allure.step('Check: user region has partners list.')
    def check_current_user_region_has_partners_list(self):
        """Проверяем, что появился список партнеров текущего региона."""
        with allure.step('Find partners list block.'):
            partners_list = self.find_elements(*SbisPageLocators.LOCATOR_SBIS_PARTNERS)
        assert len(partners_list) > 0, 'Список партнеров региона не появился.'

    @allure.step('Change region')
    def change_region(self):
        """Меняем по ссылке регион на 'Камчатский край'."""
        with allure.step('Find user region and click.'):
            self.find_element(*SbisPageLocators.LOCATOR_SBIS_REGION).click()
        with allure.step('Find new region.'):
            elem = self.wait.until(
                ec.element_to_be_clickable(SbisPageLocators.LOCATOR_SBIS_KAMCHATSKIY_REGION_LINK))
            elem.click()
        self.wait.until((ec.url_contains(KAMCHATKA_PARTIAL_URL)))

    @allure.step('Check: changed region is appears.')
    def check_new_region_appears(self):
        """Проверяем, что подставился выбранный регион."""
        with allure.step('Find changed region name.'):
            element = self.find_element(*SbisPageLocators.LOCATOR_SBIS_REGION)
        assert KAMCHATKA_REGION == element.text, 'Новый регион не появился.'

    @allure.step('Check: changed region has new partners list.')
    def check_new_region_has_new_partners_list(self, user_region_partners_list):
        """Проверяем, что со сменой региона изменился список партнеров."""
        with allure.step('Find changed region partners list block.'):
            new_region_partners_list = self.find_element(*SbisPageLocators.LOCATOR_SBIS_PARTNERS)
        assert user_region_partners_list != new_region_partners_list, 'Список партнеров не изменился.'

    @allure.step('Check: changed region in url and title.')
    def check_new_region_info_in_url_and_title(self):
        """Проверяем, что url и title содержат информацию выбранного региона."""
        url = self.browser.current_url
        title = self.browser.title
        assert EXPECTING_URL == url, 'В URL не появилась информация о выбранном регионе (Камчатский край)'
        assert EXPECTING_TITLE == title, 'В title не появилась информация о выбранном регионе (Камчатский край)'
