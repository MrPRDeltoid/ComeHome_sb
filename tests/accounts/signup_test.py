from ...common.base_test_case import BaseTestCase
from ...pages.home_page import HomePage


class SignupDialogTest(HomePage, BaseTestCase):
    """Tests for the signup dialog"""
    def test_main_elements(self):
        """Test all dialog main elements are shown"""
        dialog = HomePage.AccountsDialog
        self.click(HomePage.joinLoginButton)
        self.find_element(dialog.accountsDialog)
        assert self.get_text(dialog.header) == "Welcome\nPlease sign up for a ComeHome account."
        self.assert_element(dialog.closeButton)
        self.assert_text("Log in", dialog.link)
        self.assert_element(dialog.firstNameField, by='name')
        self.assert_element(dialog.lastNameField, by='name')
        self.assert_element(dialog.emailField, by='name')
        self.assert_element(dialog.phoneField, by='name')
        self.assert_element(dialog.passwordField, by='name')
        self.assert_attribute(dialog.signupButton, 'disabled')
        self.assert_text("Sign Up", dialog.signupButton)
        # Click close button to close dialog
        self.click(dialog.closeButton)
        self.wait_for_element_absent(dialog.accountsDialog)

    """Test missing required fields"""
    """Test incorrect email formats"""
    """Test password not meeting requirements"""
    """Test successful signup"""
