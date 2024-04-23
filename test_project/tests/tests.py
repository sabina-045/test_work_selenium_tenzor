import pytest

from service.constants import TENZOR_LINK, SBIS_LINK
from pages.sbis_page import SbisPage
from pages.tenzor_page import TenzorPage


class TestScenario:

    def test_scenario_one(self):
        sbis_page = SbisPage(browser, SBIS_LINK)
        sbis_page.open_url()
        sbis_page.go_to_contacts_page()
        sbis_page.find_and_open_tenzor_banner()
        # browser.go_to_page(TENZOR_LINK)
        self.tenzor_page.check_block_sila_v_liudiah_is_exists()
        self.tenzor_page.check_block_about_can_be_opened(driver)
        self.tenzor_page.check_fotos_have_the_same_size()

    def test_scenario_two(self, browser):
        self.sbis_page.go_to_contacts_page()
        self.sbis_page.check_current_user_region_is_showed()
        old_partners_list = self.sbis_page.check_current_user_region_has_parthners_list()
        self.sbis_page.change_region()
        self.sbis_page.check_new_region_appears()
        self.sbis_page.check_new_region_has_new_partners_list(old_partners_list)
        self.sbis_page.check_new_region_info_in_url_and_title()

