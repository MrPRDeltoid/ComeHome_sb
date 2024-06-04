from ..common.base_test_case import BaseTestCase
from ..pages.home_page import HomePage


class AccountsDialogTest(HomePage, BaseTestCase):
    """Tests for the join/login dialog"""
    def test_signup_view_elements(self):
        """Check all elements and text when showing signup view"""
        self.launchAccountsDialog()
        self.assert_exact_text("Welcome", HomePage.AccountsDialog.title)
        self.assert_exact_text("Please sign up for a ComeHome account.", HomePage.AccountsDialog.subTitle)
        self.assert_text("Already have an account?", HomePage.AccountsDialog.loginRow)
        self.assert_exact_text("Log in", HomePage.AccountsDialog.loginLink)
        self.assert_elements(HomePage.AccountsDialog.firstNameField,
                             HomePage.AccountsDialog.lastNameField,
                             HomePage.AccountsDialog.emailField,
                             HomePage.AccountsDialog.phoneField,
                             HomePage.AccountsDialog.passwordField, by='name')
        self.assert_element_absent(HomePage.AccountsDialog.forgotPasswordLink)
        self.assert_exact_text("By registering, I agree to ComeHome Terms of Use and Privacy Policy",
                               HomePage.AccountsDialog.confirmRow)
        self.assert_exact_text("Sign Up", HomePage.AccountsDialog.signupButton)
        self.closeAccountsDialog()

    def test_login_view_elements(self):
        """Check all elements and text when showing signup view"""
        self.launchAccountsDialog()
        # Switch to log in view
        self.click(HomePage.AccountsDialog.loginLink)
        self.assert_exact_text("Welcome", HomePage.AccountsDialog.title)
        self.assert_exact_text("Please log in to your account", HomePage.AccountsDialog.subTitle)
        self.assert_text("Don't have an account?", HomePage.AccountsDialog.signupRow)
        self.assert_exact_text("Sign up", HomePage.AccountsDialog.signupLink)
        self.assert_element_absent(HomePage.AccountsDialog.firstNameField)
        self.assert_element_absent(HomePage.AccountsDialog.lastNameField)
        self.assert_element_absent(HomePage.AccountsDialog.phoneField)
        self.assert_elements(HomePage.AccountsDialog.emailField,
                             HomePage.AccountsDialog.passwordField, by='name')
        self.assert_element_absent(HomePage.AccountsDialog.confirmRow)
        self.assert_exact_text("Forgot your password?", HomePage.AccountsDialog.forgotPasswordLink)
        self.assert_attribute(HomePage.AccountsDialog.forgotPasswordLink, 'href', f'{HomePage.URL}forgot-password')
        self.assert_exact_text("Log In", HomePage.AccountsDialog.loginButton)
        self.closeAccountsDialog()
