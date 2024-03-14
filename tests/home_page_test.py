from selenium.webdriver.common.keys import Keys
from ..common.base_test_case import BaseTestCase
from ..pages.home_page import HomePage


class HomePageTest(HomePage, BaseTestCase):
    """Basic tests for main home page elements"""
    def test_main_sections(self):
        """Test that all main sections are present"""
        self.assert_url(HomePage.URL)
        self.assert_title("Home | ComeHome")
        self.assert_element(HomePage.topHeader)
        self.assert_text("Find your dream home", HomePage.pageHeaderText)
        self.assert_text("Search homes in your neighborhood and find a house that's right for you.", HomePage.pageSubheaderText)
        self.assert_element(HomePage.searchBox)
        self.assert_element(HomePage.photoSection)
        self.assert_element(HomePage.footerSection)


class HeaderTest(HomePage, BaseTestCase):
    """Tests for top header bar"""
    def test_logo(self):
        """Test logo in top header"""
        self.assert_element(HomePage.headerLogo)
        image = self.get_attribute(HomePage.headerLogoImage, 'src')
        assert ".svg" in image

    def test_menu_items(self):
        """Test menu items in top header"""
        expected_items = ['Find a home', 'My home', 'Saved', 'Alerts', 'Find an agent']
        menu_links = self.find_elements(HomePage.headerMenuItems)
        for idx, link in enumerate(menu_links):
            self.assertEqual(link.text, expected_items[idx])
        self.assert_text("Join or Log in", HomePage.joinLoginButton)


class SearchTest(HomePage, BaseTestCase):
    """Tests for main search box"""
    def test_find_search(self):
        """Test searching when Find a Home option is selected"""
        address = "199 El Nido Ave"
        # Check placeholder text
        placeholder = self.get_attribute(HomePage.searchBox, 'placeholder')
        assert placeholder == "Search for a city, ZIP code or address"
        # Enter address, wait for results, and click search button
        self.send_keys(HomePage.searchBox, address)
        self.sleep(0.5)
        #self.click(HomePage.searchButton)
        # or press ENTER
        self.send_keys(HomePage.searchBox, Keys.RETURN)
        # Wait for property page to load and check correct address in title
        for _ in range(5):
            if address not in self.get_title():
                self.sleep(0.5)
        assert address in self.get_title()
