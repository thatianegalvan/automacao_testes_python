from os import wait

from selenium.webdriver.common.by import By
from .base_page import BasePage


from selenium.webdriver.common.by import By
from .base_page import BasePage


class InventoryPage(BasePage):

    CART = (By.CLASS_NAME, "shopping_cart_link")
    FILTRO = (By.CLASS_NAME, "product_sort_container")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    BTN_ADD_TO_CART = (By.XPATH, "//button[contains(@id, 'add-to-cart')]")
    BTN_REMOVE_TO_CART = (By.XPATH, "//button[contains(@id, 'remove')]")
    CART_COUNT = (By.CLASS_NAME, "shopping_cart_badge")

    
    def is_loaded(self):
        return "/inventory.html" in self.driver.current_url

    def add_to_cart_button(self, product_name: str):
         self.click(*self.BTN_ADD_TO_CART)  

    def remove_button(self, product_name: str):
        formatted_name = product_name.lower().replace(" ", "-")
        return (By.ID, f"remove-{formatted_name}")

    def add_product_by_name(self, product_name: str):
        product_locator = (By.XPATH, f"//div[@data-test='inventory-item-name' and text()='{product_name}']")
        self.add_to_cart_button(product_name)
        
    def remove_product(self, product_name: str):
        product_locator = (By.XPATH, f"//div[@data-test='inventory-item-name' and text()='{product_name}']")
        self.click(*self.BTN_REMOVE_TO_CART)

    def get_cart_quantity(self) -> str:
        try:
            return self.get_text(*self.CART_COUNT).strip()
        except Exception:
            return "0"  # Retorna "0" se o elemento não for encontrado

    def is_cart_empty(self) -> bool:
        return self.get_cart_quantity() == "0"
    

    def clicar_filtro(self):
        self.click(*self.FILTRO) 

    def select_sorting(self, option: str):
        self.select_dropdown_by_visible_text(*self.FILTRO, option)

    def show_product_by_name(self, product_name: str):
        product_locator = (By.XPATH, f"//div[@data-test='inventory-item-name' and text()='{product_name}']")
        return self.get_text(*product_locator)

    def show_product_by_price(self, price: str): 
        price_locator = (By.XPATH, f"//div[@data-test='inventory-item-price'][1]]")   
    
    def open_sidebar_menu(self):
        self.click(*self.MENU_BUTTON)

    def click_sidebar_option(self):
        option_locator = (By.ID, "reset_sidebar_link")
        self.driver.implicitly_wait(5)  # Aguarda até que o elemento esteja presente
        self.click(*option_locator)
