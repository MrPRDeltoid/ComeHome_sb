from seleniumbase import BaseCase


class BasePage(BaseCase):
    """Selectors and methods common across the app"""
    # Main top header menu items
    topHeader = '[data-hc-name="top-section"]'
    headerLogo = '[data-hc-name="logo"]'
    headerLogoImage = 'img[data-hc-name="comehome-logo"]'
    headerMenuItems = '[data-hc-name="links"] > div > button'
    joinLoginButton = '[data-hc-name="join-login-link"]'
    profileButton = '[data-hc-name="profile-button"]'
    accountMenuList = 'div[class="AuthButtonComeHome__AuthDropdown"]'
    accountMenuListItems = 'div[class="AuthButtonComeHome__AuthDropdown"] > ul > li'

    def get_account_menu_list_items(self):
        """Get the list of menu items when clicking profile button"""
        menu_items = []
        # Click on profile button and cycle through items, get text for each
        self.click(self.profileButton)
        self.wait_for_element(self.accountMenuList)
        for item in self.find_elements(self.accountMenuListItems):
            menu_items.append(item.text)
        # Close menu and return list of items
        self.click(self.profileButton)
        return menu_items

    def click_account_menu_list_item(self, wanted_item):
        """Click the given menu list item"""
        self.click(self.profileButton)
        for item in self.find_elements(self.accountMenuListItems):
            # If item matched the wanted item, click
            if item.text == wanted_item:
                item.click()
                return True
        return print(f"No such item in menu items: {wanted_item.text}")
