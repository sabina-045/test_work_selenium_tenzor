import allure
from selenium.common.exceptions import NoSuchElementException

from test_project.pages.base_page import BasePage
from test_project.service.locators import TenzorPageLocators
from test_project.service.constants import TENZOR_ABOUT_LINK


class TenzorPage(BasePage):
    """Класс страницы tenzor.ru."""

    @allure.step('Check: block "Сила в людях" exists.')
    def check_block_sila_is_exists(self):
        """Проверяем наличие блока 'Сила в людях'."""
        try:
            self.find_element(*TenzorPageLocators.LOCATOR_TENZOR_SILA_BLOCK)
        except NoSuchElementException:
            'Блок "Сила в людях" отсутствует на странице tenzor.ru'

    @allure.step('Check: block "about" can be opened.')
    def check_block_about_can_be_opened(self):
        """Проверяем, что страница 'https://tensor.ru/about' открывается."""
        with allure.step('Find block "about".'):
            element = self.find_element(*TenzorPageLocators.LOCATOR_TENZOR_PODROBNEE_LINK)
        self.browser.execute_script("arguments[0].click();", element)
        self.browser.switch_to.window(self.browser.window_handles[1])
        assert TENZOR_ABOUT_LINK == self.browser.current_url, 'Страница "https://tensor.ru/about" не открывается.'

    @allure.step('Check: images in block "Работаем" have the same size.')
    def check_fotos_have_the_same_size(self):
        """Проверяем, что фото в разделе 'Работаем' имеют одинаковый размер."""
        with allure.step('Find image.'):
            image = self.find_element(*TenzorPageLocators.LOCATOR_TENZOR_RABOTAEM_BLOCK_FOTO)
        image_size = image.size
        with allure.step('Find images.'):
            fotos = self.find_elements(*TenzorPageLocators.LOCATOR_TENZOR_RABOTAEM_BLOCK_FOTO)
        for foto in fotos:
            foto_size = foto.size
            assert foto_size == image_size, f'Размеры изображений в разделе "Работаем" не совпадают.'
