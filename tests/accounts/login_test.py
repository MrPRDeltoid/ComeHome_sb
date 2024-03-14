from ...common.base_test_case import BaseTestCase
from ...pages.home_page import HomePage


class LoginDialogTest(HomePage, BaseTestCase):
    """Tests for the login dialog"""
    def test_main_elements(self):
        """Test all dialog main elements are shown"""
        self.click(HomePage.joinLoginButton)
        self.find_element(HomePage.AccountsDialog.accountsDialog)
        # Click  login link to show login view
        dialog = HomePage.AccountsDialog
        self.click(dialog.link)
        self.assert_text("Sign up", dialog.link)
        self.assert_exact_text("Welcome\nPlease log in to your account", dialog.header)
        self.assert_element(dialog.closeButton)
        self.assert_element_absent(dialog.firstNameField, by='name')
        self.assert_element_absent(dialog.lastNameField, by='name')
        self.assert_element(dialog.emailField, by='name')
        self.assert_element_absent(dialog.phoneField, by='name')
        self.assert_element(dialog.passwordField, by='name')
        self.assert_attribute(dialog.loginButton, 'disabled')
        self.assert_text("Log In", dialog.loginButton)
        # Click close button to close dialog
        self.click(dialog.closeButton)
        self.wait_for_element_absent(dialog.accountsDialog)

    def test_successful_login(self):
        """Test successful login when supplying valid email and password"""
        email = "pcmanton@gmail.com"
        password = "Pcmgz1312"
        # Navigate to login dialog
        dialog = HomePage.AccountsDialog
        self.click(HomePage.joinLoginButton)
        self.click(dialog.link)
        self.assert_element(dialog.emailField, by='name')
        # Enter valid email and password
        self.type(dialog.emailField, email, by='name')
        self.type(dialog.passwordField, password, by='name')
        # Click Log in
        self.assert_attribute_not_present(dialog.loginButton, 'disabled')
        self.click(dialog.loginButton)
        self.wait_for_element_not_present(dialog.accountsDialog)
        # Check profile button
        self.wait_for_element(HomePage.profileButton)
        menu_items = HomePage.get_account_menu_list_items(self)
        assert menu_items == ['Your Profile', 'Settings', 'Activity', 'Logout']
        # Click Logout
        HomePage.click_account_menu_list_item(self, 'Logout')
        self.wait_for_element_absent(HomePage.profileButton)
        self.wait_for_element(HomePage.joinLoginButton)
        self.assert_element_absent(HomePage.profileButton)
