from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class RecorderTest(BaseCase):
    def test_recording(self):
        self.open("https://www.comehome.com/")
        self.type('input[name="comehome-address-search-0.7234775322837683"]', "1")
        self.type('input[name="comehome-address-search-0.5205754250078403"]', "19")
        self.type('input[name="comehome-address-search-0.04980155922583007"]', "199")
        self.type('input[name="comehome-address-search-0.365476524231767"]', "199 ")
        self.type('input[name="comehome-address-search-0.014700742879417028"]', "199 e")
        self.type('input[name="comehome-address-search-0.7890614977576651"]', "199 el")
        self.type('input[name="comehome-address-search-0.4605048596263468"]', "199 el ")
        self.type('input[name="comehome-address-search-0.30618297424750285"]', "199 el n")
        self.type('input[name="comehome-address-search-0.15697456322736092"]', "199 el ni")
        self.type('input[name="comehome-address-search-0.3363310323702857"]', "199 el nid")
        self.type('input[name="comehome-address-search-0.664339283547938"]', "199 el nido")
        self.type('input[name="comehome-address-search-0.9680445249438487"]', "199 el nido ")
        self.type('input[name="comehome-address-search-0.345124247298098"]', "199 el nido a")
        self.type('input[name="comehome-address-search-0.9335475272809737"]', "199 el nido av")
        self.type('input[name="comehome-address-search-0.9837183120876423"]', "199 el nido ave")
        self.click('li[id="199-El-Nido-Ave-Pasadena-CA-91107"]')
        self.click('button[id="radix-:r4:-trigger-MAP"]')
        self.click('button[aria-label="See more"]')
