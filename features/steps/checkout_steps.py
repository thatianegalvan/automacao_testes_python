from behave import given, when, then

from tests.pages.cart_page import CartPage
from tests.pages.checkout_page import CheckoutPage
from tests.pages.inventory_page import InventoryPage
from tests.pages.login_page import LoginPage


@given("que o usuário está logado")
def step_user_logged_in(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()
    context.login_page.login("standard_user", "secret_sauce")
    assert "inventory" in context.driver.current_url


@when("o usuário acessa o carrinho")
def access_cart(context):
    context.cart_page = CartPage(context.driver)
    context.cart_page.access_cart()                                             
    assert "cart" in context.driver.current_url



@when("o usuário inicia o checkout")
def step_start_checkout(context):
    context.cart_page = CartPage(context.driver)
    context.cart_page.click_checkout()
    assert "checkout-step-one" in context.driver.current_url

@then('o usuário preenche nome "{nome}", sobrenome "{sobrenome}" e CEP "{cep}"')
def step_fill_checkout_information(context, nome, sobrenome, cep):
    context.checkout_page = CheckoutPage(context.driver)
    context.checkout_page.fill_form(nome, sobrenome, cep)
    assert "checkout-step-two" in context.driver.current_url


@when("o usuário finaliza a compra")
def step_finish_purchase(context):
    context.checkout_page.finish()
    assert "checkout-complete" in context.driver.current_url


@then("uma mensagem de confirmação deve ser exibida")
def step_validate_confirmation_message(context):
    mensagem_confirmacao = context.checkout_page.get_success_message()
    assert mensagem_confirmacao == "Thank you for your order!"