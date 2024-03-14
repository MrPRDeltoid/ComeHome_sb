from ...common.base_test_case import BaseTestCase
from ...pages.home_page import HomePage, SignupDialog


class LoginDialogTest(HomePage, BaseTestCase):
    """Tests for the login dialog"""
    def test_main_elements(self):
        """Test all dialog main elements are shown"""
        self.click(HomePage.joinLoginButton)
        self.find_element(HomePage.loginDialog)
        # Click  login link to show login view
        self.click(SignupDialog.link)
        self.assert_text("Sign up",SignupDialog.link)
        self.assert_exact_text("Welcome\nPlease log in to your account", SignupDialog.header)
        self.assert_element(SignupDialog.closeButton)
        self.assert_element_absent(SignupDialog.firstNameField, by='name')
        self.assert_element_absent(SignupDialog.lastNameField, by='name')
        self.assert_element(SignupDialog.emailField, by='name')
        self.assert_element_absent(SignupDialog.phoneField, by='name')
        self.assert_element(SignupDialog.passwordField, by='name')
        self.assert_attribute(SignupDialog.loginButton, 'disabled')
        self.assert_text("Log In", SignupDialog.loginButton)
        # Click close button to close dialog
        self.click(SignupDialog.closeButton)
        self.wait_for_element_absent(HomePage.loginDialog)

    def test_successful_login(self):
        """Test successful login when supplying valid email and password"""
        email = "pcmanton@gmail.com"
        password = "Pcmgz1312"
        # Navigate to login dialog
        self.click(HomePage.joinLoginButton)
        self.click(SignupDialog.link)
        self.assert_element(SignupDialog.emailField, by='name')
        # Enter valid email and password
        self.type(SignupDialog.emailField, email, by='name')
        self.type(SignupDialog.passwordField, password, by='name')
        # Click Log in
        self.assert_attribute_not_present(SignupDialog.loginButton, 'disabled')
        self.click(SignupDialog.loginButton)
        self.wait_for_element_not_present(HomePage.loginDialog)
        # Check profile button
        self.wait_for_element(HomePage.profileButton)
        menu_items = HomePage.get_account_menu_list_items(self)
        assert menu_items == ['Your Profile', 'Settings', 'Activity', 'Logout']
        # Click Logout
        HomePage.click_account_menu_list_item(self, 'Logout')
        self.wait_for_element_absent(HomePage.profileButton)
        self.wait_for_element(HomePage.joinLoginButton)
        self.assert_element_absent(HomePage.profileButton)
