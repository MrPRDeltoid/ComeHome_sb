from .base_page import BasePage


class PropertyPage(BasePage):
    """Elements common to both views"""
    breadcrumbsSection = '[data-hc-name="breadcrumbs"]'
    breadcrumbs = '.Breadcrumbs__link'
    publicViewButton = '[data-hc-name="public-view-button"]'
    ownerViewButton = '[data-hc-name="owner-view-button"]'


class PublicView(PropertyPage):
    """Elements and methods specific to Public View"""
    def get_url(self, slug):
        URL = f"{BasePage.BASE_URL}property-details/{slug}"
        return URL

    def get_title(self, address):
        TITLE = f"{address} | Property Details | ComeHome"
        return TITLE

    photoSection = '[data-hc-name="carousel-section"]'
    introSection = '[data-hc-name="property-intro-section"]'
    introSectionAddress = '.PropertyIntro__Address'
    introSectionDetails = '[data-hc-name="property-info"]'
    propertyDetailsSection = '[class$="__AdditionalHomeDetails"]'
    summaryOptionsPanel = '[data-hc-name="summary-options-panel"]'
    upsellSection = '[data-hc-name="upsell-section"]'
    mapViewSection = 'section[class^="MapPropertyPage__MapPropertyPage"]'

    # Methods


class OwnerView(PropertyPage):
    """Elements and methods specific to Owner View"""
    def get_url(self, slug):
        URL = f"{BasePage.BASE_URL}homeowner/{slug}"
        return URL

    def get_title(self, address):
        TITLE = f"{address} | My Home | ComeHome"
        return TITLE

    avmSection = '[data-hc-name="avm-section"]'
    avmSectionAddress = '[data-hc-name="avm-address"] > h1'
    avmSectionDetails = '[data-hc-name="avm-property-details"]'
    avmSectionTitle = '[data-hc-name="avm-title"]'
    avmSectionValue = '[data-hc-name="avm-value"]'
    brokerageSection = 'class$="__BrokerageAttribution"]'
    yourHomeSection = '[data-hc-name="ho-dashboard-section-your_home"]'
    yourNeighborhoodSection = '[data-hc-name="ho-dashboard-section-your_neighborhood"]'
    toolsAndInsightsSection = '[data-hc-name="ho-dashboard-section-tools_and_insights"]'

    # Methods
