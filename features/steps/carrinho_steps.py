from behave import given, when, then

from tests.pages.cart_page import CartPage
from tests.pages.inventory_page import InventoryPage
from tests.pages.login_page import LoginPage


@given("que o usuário está logado e possui um produto no carrinho")
def step_user_with_product_in_cart(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()
    context.login_page.login("standard_user", "secret_sauce")

    context.inventory_page = InventoryPage(context.driver)
    context.inventory_page.add_backpack_to_cart()


@when("o usuário navega até a página do carrinho")
def step_navigate_to_cart(context):
    context.inventory_page.open_cart()
    context.cart_page = CartPage(context.driver)
    assert "cart" in context.driver.current_url


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


