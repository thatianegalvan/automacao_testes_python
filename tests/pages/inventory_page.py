from selenium.webdriver.common.by import By
from .base_page import BasePage


class InventoryPage(BasePage):

    ADD_MOCHILA = (By.ID, "add-to-cart-sauce-labs-backpack")
    CARRINHO = (By.CLASS_NAME, "shopping_cart_link")

    def add_product(self):
        self.click(*self.ADD_MOCHILA)

    def go_to_cart(self):
        self.click(*self.CARRINHO)