from pages.base_page import BasePage
from components.components import WebElement

class Offtoppages(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://www.saucedemo.com/'
        super().__init__(driver, self.base_url)

        self.username = WebElement(driver, '#user-name')
        self.password = WebElement(driver, '#password')
        self.login = WebElement(driver,"#login-button")
        self.btn_1_item = WebElement(driver, "#add-to-cart-sauce-labs-backpack")
        self.btn_2_item = WebElement(driver, "#add-to-cart-sauce-labs-bike-light")
        self.btn_shop = WebElement(driver, '#shopping_cart_container > a')
        self.btn_1_item_remove = WebElement(driver, '#remove-sauce-labs-backpack')
        self.btn_2_item_remove = WebElement(driver, '#remove-sauce-labs-bike-light')

    def get_text(self):
        str(self.find_element().text)