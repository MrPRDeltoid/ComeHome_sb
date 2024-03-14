from ...common.base_test_case import BaseTestCase
from ...pages.home_page import HomePage, SignupDialog


class SignupDialogTest(HomePage, BaseTestCase):
    """Tests for the signup dialog"""
    def test_main_elements(self):
        """Test all dialog main elements are shown"""
        self.click(HomePage.joinLoginButton)
        self.find_element(HomePage.loginDialog)
        assert self.get_text(SignupDialog.header) == "Welcome\nPlease sign up for a ComeHome account."
        self.assert_element(SignupDialog.closeButton)
        self.assert_text("Log in", SignupDialog.link)
        self.assert_element(SignupDialog.firstNameField, by='name')
        self.assert_element(SignupDialog.lastNameField, by='name')
        self.assert_element(SignupDialog.emailField, by='name')
        self.assert_element(SignupDialog.phoneField, by='name')
        self.assert_element(SignupDialog.passwordField, by='name')
        self.assert_attribute(SignupDialog.signupButton, 'disabled')
        self.assert_text("Sign Up", SignupDialog.signupButton)
        # Click close button to close dialog
        self.click(SignupDialog.closeButton)
        self.wait_for_element_absent(HomePage.loginDialog)

    """Test missing required fields"""
    """Test incorrect email formats"""
    """Test password not meeting requirements"""
    """Test successful signup"""
