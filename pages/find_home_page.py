from .base_page import BasePage


class FindHomePage(BasePage):
    """Elements shown on page after clicking Find a Home in main header"""
    URL = "https://www.comehome.com/search"
    searchBar = '[data-hc-name="toolbar"]'
    mapSection = '[data-hc-name="map-section"]'
    cardSection = '[data-hc-name="property-card-section"]'

    # Methods
    def gotoFindHomePage(self):
        self.goto(self.URL)
