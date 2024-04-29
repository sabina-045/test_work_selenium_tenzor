from selenium.webdriver.common.by import By


class SbisPageLocators:
    """Класс локаторов для SbisPage"""
    LOCATOR_SBIS_CONTACTS_LINK = (By.CSS_SELECTOR, '[href="/contacts"]')
    LOCATOR_SBIS_BANNER_TENZOR_LINK = (By.CSS_SELECTOR, '[href="https://tensor.ru/"]')
    LOCATOR_SBIS_REGION = (By.CSS_SELECTOR, '.sbis_ru-Region-Chooser__text.sbis_ru-link')
    LOCATOR_SBIS_PARTNERS = (By.CSS_SELECTOR, '.sbisru-Contacts-List__name')
    LOCATOR_SBIS_KAMCHATSKIY_REGION_LINK = (
        By.CSS_SELECTOR,
        '.sbis_ru-Region-Panel__list-l .sbis_ru-Region-Panel__item:nth-child(43)')
    LOCATOR_SBIS_FOOTER_LINK = (
        By.XPATH,
        '//div[@class="sbisru-Footer__container"]/div[3]/ul/li[8]/a')
    LOCATOR_SBIS_PLAGIN_BUTTON = (
        By.XPATH,
        '//div[@class="sbis_ru-VerticalTabs__left"]/div[contains(@sbisname, "TabButtons")]/div[2]')
    LOCATOR_SBIS_PLAGIN_DOWNLOAD_LINK = (
        By.XPATH,
        '//a[@href="https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]')

class TenzorPageLocators:
    """Класс локаторов для TenzorPage"""
    LOCATOR_TENZOR_SILA_BLOCK = (By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg')
    LOCATOR_TENZOR_PODROBNEE_LINK = (By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg [href="/about"]')
    LOCATOR_TENZOR_RABOTAEM_BLOCK_FOTO = (By.CSS_SELECTOR, '.tensor_ru-About__block3 img')
