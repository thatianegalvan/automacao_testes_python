from behave import given, when, then

from tests.pages.cart_page import CartPage
from tests.pages.inventory_page import InventoryPage
from tests.pages.login_page import LoginPage


@then('o produto "{nome_produto}" deve estar presente no carrinho')
def step_validate_product_in_cart(context, nome_produto):
    context.cart_page = CartPage(context.driver)
    assert context.cart_page.is_product_in_cart(nome_produto), f"O produto '{nome_produto}' não está presente no carrinho."     

@when("o usuário remove o produto do carrinho")
def step_remove_product_from_cart(context):
    # Utiliza a transação ou o método de remoção da CartPage
    context.cart_page.remove_item()


@then("o carrinho deve ficar vazio")
def step_validate_empty_cart(context):
    # Valida que o item não está mais visível/presente na lista
    assert context.cart_page.is_cart_empty()


@then("o usuário clica em continuar comprando")
def step_continue_shopping(context):
    context.cart_page.click_continue_shopping()


@then("deve ser redirecionado de volta para a página de inventário")
def step_validate_return_to_inventory(context):
    assert "inventory" in context.driver.current_url


