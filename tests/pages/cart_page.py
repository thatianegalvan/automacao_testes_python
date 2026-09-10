from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.common.by import By
class CartPage(BasePage):
    CHECKOUT = (By.ID, "checkout")
    CART = (By.ID, "shopping_cart_container")

    def start_checkout(self):
        self.click(*self.CHECKOUT)

    def click_checkout(self):
        self.start_checkout()

    def is_cart_empty(self):
      #  return "Your cart is empty" in self.driver.page_source
        items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        return len(items) == 0
    
    def access_cart(self):
        self.click(*self.CART)
        

    def is_product_in_cart(self, product_name):
        cart_list = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        for item in cart_list:
            item_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            if item_name == product_name:
                return True
        return False    