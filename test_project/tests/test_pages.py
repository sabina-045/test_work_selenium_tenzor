import allure

from test_project.service.constants import TENZOR_LINK, SBIS_LINK
from test_project.pages.sbis_page import SbisPage
from test_project.pages.tenzor_page import TenzorPage


@allure.feature('Scenario_one')
def test_scenario_one(browser):
    sbis_page = SbisPage(browser, SBIS_LINK)
    sbis_page.go_to_contacts_page()
    sbis_page.find_and_open_tenzor_banner()
    browser.switch_to.window(browser.window_handles[1])
    tenzor_page = TenzorPage(browser, TENZOR_LINK)
    tenzor_page.check_block_sila_is_exists()
    tenzor_page.check_block_about_can_be_opened()
    tenzor_page.check_fotos_have_the_same_size()


@allure.feature('Scenario_two')
def test_scenario_two(browser):
    sbis_page = SbisPage(browser, SBIS_LINK)
    sbis_page.go_to_contacts_page()
    sbis_page.check_current_user_region_is_showed()
    user_region_partners_list = sbis_page.check_current_user_region_has_partners_list()
    sbis_page.change_region()
    sbis_page.check_new_region_appears()
    sbis_page.check_new_region_has_new_partners_list(user_region_partners_list)
    sbis_page.check_new_region_info_in_url_and_title()
