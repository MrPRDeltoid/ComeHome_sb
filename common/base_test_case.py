from seleniumbase import BaseCase
from ..pages.base_page import BasePage


class BaseTestCase(BaseCase):
    """Common methods used across tests"""
    def setUp(self):
        super().setUp()
        self.open(BasePage.BASE_URL)
        #options = self.driver.ChromeOptions()
        self.maximize_window()

    def tearDown(self):
        self.save_teardown_screenshot()
        super().tearDown()
