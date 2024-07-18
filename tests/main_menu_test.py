from ..common.base_test_case import BaseTestCase
from ..pages.home_page import HomePage
from ..pages.find_home_page import FindHomePage


class HeaderTest(HomePage, BaseTestCase):
    """Tests for main header bar"""
    def test_main_menu_elements(self):
        """Test menu items in top header"""
        self.assert_element(HomePage.MainMenu.logo)  # TODO: Convert to visual assertion?
        self.assert_exact_text("Find a home", HomePage.MainMenu.buyHomeButton)
        self.assert_exact_text("My home", HomePage.MainMenu.myHomeButton)
        self.assert_exact_text("Saved", HomePage.MainMenu.savedButton)
        self.assert_exact_text("Alerts", HomePage.MainMenu.alertsButton)
        self.assert_exact_text("Find an agent", HomePage.MainMenu.findAnAgentButton)
        self.assert_exact_text("Join or Log in", HomePage.MainMenu.joinLoginButton)  # TODO: Convert to visual assertion?


class ClickOptionsTest(HomePage, BaseTestCase):
    """Tests for clicking on each of the main menu options"""
    def test_click_find_a_home(self):
        """Check that clicking Find a home shows correct page"""
        self.click(HomePage.MainMenu.buyHomeButton)
        self.assert_title("Real estate and homes for sale | ComeHome")
        self.assert_elements(FindHomePage.MainMenu.mainMenu,
                             FindHomePage.searchBar,
                             FindHomePage.mapSection,
                             FindHomePage.cardSection)

    # def test_click_my_home(self):
    #     """Check that clicking My home shows correct page"""
    #
    # def test_click_saved(self):
    #     """Check that clicking Saved shows correct page"""
    #
    # def test_click_alerts(self):
    #     """Check that clicking Alerts shows correct page"""
    #
    # def test_click_find_agent(self):
    #     """Check that clicking Find an agent shows correct page"""
