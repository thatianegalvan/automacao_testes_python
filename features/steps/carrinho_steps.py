from behave import given, when, then

from tests.pages.cart_page import CartPage
from tests.pages.inventory_page import InventoryPage
from tests.pages.login_page import LoginPage


@then('o produto "{nome_produto}" deve estar presente no carrinho')
def validate_product_in_cart(context, nome_produto):
    context.cart_page = CartPage(context.driver)
    
    is_present = context.cart_page.is_product_in_cart(nome_produto)
    
    # Se is_present for False, exibe mensagem exibindo os itens que realmente estavam na tela
    items_found = context.cart_page.get_all_cart_item_names()
    assert is_present, f"O produto '{nome_produto}' não foi encontrado no carrinho! Itens presentes: {items_found}"

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

@when("o usuário retorna para a página de produtos")
def step_return_to_inventory(context):
    context.cart_page = CartPage(context.driver)
    context.cart_page.click_continue_shopping()
   


