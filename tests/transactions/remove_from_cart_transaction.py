
from guara.transaction import AbstractTransaction
from tests.pages.inventory_page import InventoryPage

class RemoveFromCartTransaction(AbstractTransaction):

    def do(self):

        pagina = InventoryPage(self._driver)
        pagina.remove_product()

        self.resultado = (
            pagina.is_cart_badge_displayed()
        )
        return self._driver.current_url
    
    def get_result(self):
        return self.resultado