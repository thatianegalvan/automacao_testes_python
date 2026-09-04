from selenium.webdriver.common.by import By
from .base_page import BasePage


class InventoryPage(BasePage):
    

    ADD_MOCHILA = (By.ID, "add-to-cart-sauce-labs-backpack")
    CARRINHO = (By.CLASS_NAME, "shopping_cart_link")

    def is_loaded(self):
        return  "/inventory.html" in self.driver.current_url

    def add_product(self):
        self.click(*self.ADD_MOCHILA)

    def go_to_cart(self):
        self.click(*self.CARRINHO)

    def open_cart(self):
        self.go_to_cart()

    def remove_product(self):
        self.click(*self.ADD_MOCHILA)   ##verificar o botão que remove o produto do carrinho, pois o mesmo botão que adiciona o produto ao carrinho, também remove o produto do carrinho.

    def get_cart_quantity(self):
        return self.get_text(*self.CARRINHO)