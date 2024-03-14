from .base_page import BasePage


class SignupDialog(BasePage):
    """Selectors in the login dialog"""
    header = '[data-hc-name="modal-header"]'
    link = 'button[class*="SignUpOrLoginLink__"]'
    closeButton = '[data-hc-name="close-dialog-button"]'
    firstNameField = 'firstname'
    lastNameField = 'lastname'
    emailField = 'email'
    phoneField = 'phone'
    passwordField = 'password'
    confirmCheckbox = 'div[data-hc-name="confirm-row"] > div > div > input'
    signupButton = '[data-hc-name="signup-button"] > button'
    loginButton = 'button[aria-label="log in"]'

    #def close_dialog(self):
        #"""Click the close(x) button in header"""
        #self.click(self.closeButton)
        #self.wait_for_element_absent(HomePage.loginDialog)

    #def login(self, first, last, email, password, phone=''):
        #"""Fill out login dialog fields and click login"""


class HomePage(BasePage):
    """Selectors and methods for home page"""
    URL = "https://www.comehome.com/"

    # Main page items
    pageHeaderText = 'h1[class="HomeSubpageSearch__Header"]'
    pageSubheaderText = 'div[class*="HomeSubpageSearch__SubHeader"]'
    searchTypeButtons = 'div[class="HomeSubpageSearch__SearchTypeSelector"]'
    searchBox = '[data-hc-name="search-field"] > div > div > input'
    searchButton = 'button[class*="HomeSubpageSearch__SearchButton"]'
    photoSection = 'div[class="HomeSubpageSearch__PhotoSection"]'
    footerSection = '[data-hc-name="footer-section"]'

    # Login dialog
    loginDialog = 'div[class*="AuthModal__Modal"]'
