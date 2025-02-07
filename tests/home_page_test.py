import json
from ..common.base_test_case import BaseTestCase
from ..pages.home_page import HomePage
from ..pages.property_page import PropertyPage, PublicView, OwnerView


class HomePageTest(HomePage, BaseTestCase):
    """Basic tests for main home page elements"""
    def test_main_sections_exist(self):
        """Test that all main sections are present"""
        self.assert_elements(HomePage.MainMenu.mainMenu,
                             HomePage.topSection,
                             HomePage.photoSection,
                             HomePage.trackOrBuyHomeSection,
                             HomePage.yourTeamAgentSection,
                             HomePage.FooterSection.footerSection)

    def test_url_and_title(self):
        self.assert_url(HomePage.URL)
        self.assert_title("Home | ComeHome")


class FindHomeSearchTest(HomePage, PropertyPage, BaseTestCase):
    """Tests for search section when Find a home is selected"""
    def test_elements_and_text(self):
        """Check correct elements and text are shown"""
        self.assert_exact_text("Find your dream home", HomePage.pageHeaderText)
        self.assert_exact_text("Search homes in your neighborhood and find a house that's right for you.",
                               HomePage.pageSubheaderText)
        self.assert_exact_text("Find a home", HomePage.findHomeButton)
        self.assert_elements(HomePage.searchField,
                             HomePage.searchButton)
        self.assert_attribute(HomePage.searchField, 'placeholder', "Search for a city, ZIP code or address")

    def test_search(self):
        """Test searching with valid address"""
        # Get data from file
        property_data = json.loads(self.get_file_data(r'..\data\properties.json'))['property1']
        # Search for the street
        HomePage.searchForProperty(self, property_data['street'])
        # Check correct url and address in property page title
        self.assert_url_contains("property-details")
        self.assert_title_contains(property_data['street'])
        # Check correct breadcrumb values
        self.assert_exact_text(f"Home{property_data['city']}, {property_data['state']}{property_data['zip']}{property_data['street']}",
                               PropertyPage.breadcrumbsSection)
        # Verify state of view buttons
        self.assert_attribute(PropertyPage.publicViewButton, 'data-state', 'active')
        self.assert_attribute(PropertyPage.ownerViewButton, 'data-state', 'inactive')
        # Verify property details header
        self.assert_exact_text(f"{property_data['street']}., {property_data['city']}, {property_data['state']} {property_data['zip']}",
                               PublicView.introSectionAddress)
        self.assert_exact_text(f"{property_data['type']}\n{property_data['beds']} Beds\n{property_data['baths']} Baths\n{property_data['gla']} Sq Ft",
                               PublicView.introSectionDetails)


class MyHomeSearchTest(HomePage, BaseTestCase):
    """Tests for search section when My home value is selected"""
    def test_elements_and_text(self):
        """Check correct elements and text are shown"""
        # Switch to My home value view
        self.click(HomePage.trackHomeButton)
        self.assert_exact_text("See your home's \nfull potential", HomePage.pageHeaderText)
        self.assert_exact_text("Claim your home and unlock features to see your home's value, equity, and more.",
                               HomePage.pageSubheaderText)
        self.assert_exact_text("My home value", HomePage.trackHomeButton)
        self.assert_elements(HomePage.searchField,
                             HomePage.searchButton)
        self.assert_attribute(HomePage.searchField, 'placeholder', "Enter your home address")

    def test_search(self):
        """Test searching with valid address"""
        # Get data from file
        property_data = json.loads(self.get_file_data(r'..\data\properties.json'))['property1']
        # Switch to My home value view
        self.click(HomePage.trackHomeButton)
        # Search for the street
        HomePage.searchForProperty(self, property_data['street'])
        # Check correct url and address in homeowner page title
        self.assert_url_contains("homeowner")
        self.assert_title_contains(property_data['street'])
        # Verify AVM section address and details
        self.assert_exact_text(property_data['street'], OwnerView.avmSectionAddress)
        self.assert_exact_text(f"{property_data['beds']} Bed\n|\n{property_data['baths']} Bath\n|\n{property_data['gla'].replace(',', '')} Sq Ft.",
                               OwnerView.avmSectionDetails)


class TrackBuyHomeTest(HomePage, BaseTestCase):
    """Tests for track or buy home section"""
    def test_elements_and_text(self):
        """Check correct elements and text are displayed"""
        self.scroll_into_view(HomePage.trackOrBuyHomeSection)
        self.assert_exact_text("Buying a home", HomePage.buyHomeTitle)
        self.assert_exact_text("Search homes for sale and filter by price, neighborhood, school ratings, and more. Find the perfect home that fits your needs.",
                               HomePage.buyHomeDescription)
        self.assert_exact_text("Search homes", HomePage.searchHomesButton)
        self.is_element_enabled(HomePage.searchHomesButton)
        self.assert_attribute(HomePage.searchHomesButton, 'href', f'{HomePage.URL}search')
        self.assert_exact_text("Your homeowner dashboard", HomePage.yourHomeTitle)
        self.assert_exact_text("See your home's value, equity, and what a home renovation would do to your value. Claim your home and access these features and more.",
                               HomePage.yourHomeDescription)
        self.assert_exact_text("See my home", HomePage.seeMyHomeButton)
        self.is_element_enabled(HomePage.seeMyHomeButton)
        self.assert_attribute(HomePage.seeMyHomeButton, 'href', f'{HomePage.URL}homeowner')


class FindAgentTest(HomePage, BaseTestCase):
    """Tests for find an agent section"""
    def test_elements_and_text(self):
        """Check correct elements and text are displayed"""
        self.scroll_into_view(HomePage.findAgentSection)
        self.assert_exact_text("Need help finding an agent? We'll connect you.", HomePage.findAgentTitle)
        self.assert_exact_text("We can help pair you with the right agent for your real estate needs. Let our team help make locating the best agent easy and smooth.",
                               HomePage.findAgentDescription)
        self.assert_exact_text("Learn More", HomePage.findAgentButton)
        self.is_element_enabled(HomePage.findAgentButton)
        self.assert_attribute(HomePage.findAgentButton, 'href', f'{HomePage.URL}concierge-team')
