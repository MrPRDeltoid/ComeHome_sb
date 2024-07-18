from seleniumbase import BaseCase


class Header(BaseCase):
    """Selectors and methods for the main header"""
    logo = '[data-hc-name="logo"] > button[data-hc-name="comehome-logo"]'
    buyHomeButton = '[data-hc-name="buy-home-button"]'
    myHomeButton = '[data-hc-name="my-home-button"]'
    savedButton = '[data-hc-name="saved-button"]'
    alertsButton = '[data-hc-name="alerts-button"]'
    findAnAgentButton = '[data-hc-name="find-an-agent-button"]'
    # When not logged in
    joinLoginButton = '[data-hc-name="join-login-link"]'
    # When logged in
    profileButton = '[data-hc-name="profile-button"]'
    accountMenuList = 'div[class="AuthButtonComeHome__AuthDropdown"]'
    accountMenuListItems = 'div[class="AuthButtonComeHome__AuthDropdown"] > ul > li'


class Dialog(BaseCase):
    """Selectors and methods for the join/login dialog"""
    header = '[data-hc-name="modal-header"]'
    closeButton = '[data-hc-name="close-dialog-button"]'
    title = '[class="AuthModal__Title"]'
    subTitle = '[class="AuthModal__Subtitle"]'
    loginRow = '[data-hc-name="log-in-row"]'
    loginLink = '[data-event-name="click_login_cta"]'
    signupRow = '[data-hc-name="sign-up-row"]'
    signupLink = '[data-event-name="click_signup_cta"]'
    firstNameField = 'firstname'
    lastNameField = 'lastname'
    emailField = 'email'
    phoneField = 'phone'
    passwordField = 'password'
    forgotPasswordLink = '[data-hc-name="forgot-password-link"]'
    confirmRow = '[data-hc-name="confirm-row"]'
    confirmCheckbox = 'div[data-hc-name="confirm-row"] > div > div > input'
    signupButton = '[data-hc-name="signup-button"] > button'
    loginButton = 'button[aria-label="log in"]'


class Footer(BaseCase):
    pass


class BasePage(BaseCase):
    """Selectors and methods common across the app"""
    BASE_URL = "https://www.comehome.com/"

    class MainMenu(Header):
        mainMenu = '[data-hc-name="top-section"]'

    class AccountsDialog(Dialog):
        accountsDialog = 'div[class*="AuthModal__Modal"]'

    class FooterSection(Footer):
        footerSection = '[data-hc-name="footer-section"]'

    # Methods
    def launchAccountsDialog(self):
        self.click(self.MainMenu.joinLoginButton)
        self.wait_for_element(self.AccountsDialog.accountsDialog)

    def closeAccountsDialog(self):
        self.click(self.AccountsDialog.closeButton)
        self.wait_for_element_absent(self.AccountsDialog.accountsDialog)
