from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.common.by import By
class CartPage(BasePage):
    CHECKOUT = (By.ID, "checkout")
    CART = (By.ID, "shopping_cart_container")
    ITEMS_NAMES = (By.XPATH, "//*[@data-test='inventory-item-name']")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")

    def start_checkout(self):
        self.click(*self.CHECKOUT)

    def click_checkout(self):
        self.click(*self.CHECKOUT)
       # self.start_checkout()

    def click_continue_shopping(self):
        self.click(*self.CONTINUE_SHOPPING)    

    def is_cart_empty(self):
      #  return "Your cart is empty" in self.driver.page_source
        items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        return len(items) == 0
    
    def access_cart(self):
        self.click(*self.CART)
        

    def is_product_in_cart(self, product_name: str) -> bool:
        """
        Percorre todos os itens visíveis no carrinho usando um laço 'for'
        e retorna True se encontrar o produto desejado.
        """
        # Pega a lista de WebElements presentes na página
        cart_items = self.driver.find_elements(*self.ITEMS_NAMES)
        
        # Percorre a lista elemento por elemento
        for item in cart_items:
            # Pega o texto do elemento atual e remove espaços das pontas
            item_name = item.text.strip()
            
            # Se o nome for igual ao procurado, confirma a presença
            if item_name == product_name:
                return True
                
        # Se percorreu toda a lista e não encontrou
        return False

    def get_all_cart_item_names(self) -> list:
        """
        Retorna uma lista com os nomes de todos os produtos presentes no carrinho.
        Útil para depuração ou validações completas.
        """
        cart_items = self.driver.find_elements(*self.ITEMS_NAMES)
        return [item.text.strip() for item in cart_items]

    