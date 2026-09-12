
import time

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
    CROSS_BUTTON = (By.ID, "react-burger-cross-btn")
    BURGER_MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    RESET_APP_STATE_LINK = (By.ID, "reset_sidebar_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    
    def is_loaded(self):
        return "/inventory.html" in self.driver.current_url

    def add_to_cart_button(self, product_name: str):
         self.click(*self.BTN_ADD_TO_CART)  

    def remove_button(self, product_name: str):
        formatted_name = product_name.lower().replace(" ", "-")
        return (By.ID, f"remove-{formatted_name}")

    def add_product_by_name(self, product_name: str):
        xpath = f"//div[@data-test='inventory-item-name' and text()='{product_name}']/ancestor::div[@data-test='inventory-item']//button"
        self.driver.implicitly_wait(2)
        self.click(By.XPATH, xpath)  

    def remove_product_by_name(self, product_name: str):
        product_locator = (By.XPATH, f"//div[@data-test='inventory-item-name' and text()='{product_name}']")
        self.click(*self.BTN_REMOVE_TO_CART)

    def remove_product(self):
        self.driver.implicitly_wait(2) 
        remove_buttons = self.driver.find_elements(*self.BTN_REMOVE_TO_CART)
        for button in remove_buttons:
            button.click()
    
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
        self.driver.implicitly_wait(2)  # Aguarda até que o elemento esteja presente
        self.click(*option_locator)

    def click_open_sidebar_menu(self): 
        self.click(*self.CROSS_BUTTON)   

    def click_all_items_option(self):
        option_locator = (By.ID, "inventory_sidebar_link")
        self.driver.implicitly_wait(2) 
        self.click(*option_locator)

    def reset_app_state(self):
        self.click(*self.BURGER_MENU_BUTTON)
        self.click(*self.RESET_APP_STATE_LINK)

    def is_cart_badge_displayed(self) -> bool:
        """Verifica se o contador vermelho do carrinho está visível no DOM."""
        elements = self.driver.find_elements(*self.CART_BADGE)
        return len(elements) > 0 and elements[0].is_displayed()

    def go_to_cart(self):
        self.click(*self.CART)

    def add_product(self):
        self.click(*self.BTN_ADD_TO_CART)

