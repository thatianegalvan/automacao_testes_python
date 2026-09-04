from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.common.by import By
class CartPage(BasePage):
    CHECKOUT = (By.ID, "checkout")

    def start_checkout(self):
        self.click(*self.CHECKOUT)

    def click_checkout(self):
        self.start_checkout()

    def is_cart_empty(self):
      #  return "Your cart is empty" in self.driver.page_source
        items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        return len(items) == 0