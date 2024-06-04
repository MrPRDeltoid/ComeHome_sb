from .base_page import BasePage


class HomePage(BasePage):
    """Selectors and methods for home page"""
    URL = "https://www.comehome.com/"

    # Home Page main sections
    topSection = '[class$="__TopSection"]'
    photoSection = '[class$="__PhotoSection"]'
    trackOrBuyHomeSection = '[class$="__HomeSubpageTrackOrBuyHome"]'
    yourTeamAgentSection = '[class$="__HomeSubpageYourTeamAgent"]'
    # Page headers
    pageHeaderText = 'h1[class="HomeSubpageSearch__Header"]'
    pageSubheaderText = 'div[class*="HomeSubpageSearch__SubHeader"]'
    # Property search
    findHomeButton = '[data-hc-name="find-a-home"]'
    trackHomeButton = '[data-hc-name="track-my-home"]'
    searchField = '[data-hc-name="search-field"] > div > div > input'
    searchButton = 'button[class*="HomeSubpageSearch__SearchButton"]'
    # Photo section
    photoColumn = 'class$="__PhotoColumn"]'
    photo = '[class$="__PhotoColumnPhoto"]'
    # Track or buy home section
    buyHomeTitle = '[data-hc-name="buy-home-modal-header"]'
    buyHomeDescription = '[data-hc-name="buy-home-modal-description"]'
    searchHomesButton = '[data-hc-name="buy-home-modal-button"]'
    yourHomeTitle = '[data-hc-name="your-home-dash-modal-header"]'
    yourHomeDescription = '[data-hc-name="your-home-dash-modal-description"]'
    seeMyHomeButton = '[data-hc-name="your-home-dash-modal-button"]'
    # Find agent section
    findAgentTitle = '.HomeSubpageYourTeamAgent__CardHeader'
    findAgentDescription = '.HomeSubpageYourTeamAgent__CardDescription'
    findAgentButton = '[data-hc-name="find-an-agent-cta"]'

    # Methods
    def gotoHomePage(self):
        self.goto(self.URL)

    def searchForProperty(self, address):
        self.type(self.searchField, address)
        self.wait(0.5)  # TODO: Remove wait with a for loop
        self.click(self.searchButton)
