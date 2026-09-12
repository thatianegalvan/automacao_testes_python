from tests.pages.inventory_page import InventoryPage
from guara.transaction import AbstractTransaction
from tests.pages.inventory_page import InventoryPage

class RemoveFromCartTransaction(AbstractTransaction):

    def __init__(self, app):

        self.driver = app.driver

        pagina = InventoryPage(
            self.driver
        )

        pagina.remove_product()

        self.resultado = (
            pagina.is_cart_badge_displayed()
        )

    def value(self):
        return self.resultado