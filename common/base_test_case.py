from seleniumbase import BaseCase
from ..pages.home_page import HomePage


class BaseTestCase(BaseCase):
    """Common methods used across tests"""
    def setUp(self):
        super().setUp()
        self.open(HomePage.URL)
        #options = self.driver.ChromeOptions()
        self.maximize_window()

    def tearDown(self):
        self.save_teardown_screenshot()
        super().tearDown()
