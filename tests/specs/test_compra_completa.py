from guara.application import Application
from guara import it

from tests.transactions.login_transaction import (LoginWith)

from tests.transactions.add_to_cart_transaction import (AddToCartTransaction)

from tests.transactions.checkout_transaction import (CheckoutTransaction)

from tests.transactions.finish_order_transaction import (FinishOrderTransaction)


def test_compra_completa(driver):

    app = Application(driver)

    app.given(
        LoginWith,
        url="https://www.saucedemo.com",
        user="standard_user",
        password="secret_sauce"
    ).then(
        it.Contains,
        "inventory"
    )

    app.when(
        AddToCartTransaction
    ).asserts(
        it.Contains,
        "cart"
    )

    app.when(
        CheckoutTransaction,
        name="Thatiane",
        last="Teste",
        zip_code="12345"
    ).asserts(
        it.Contains,
        "checkout-step-two"
    )

    app.when(
        FinishOrderTransaction
    ).asserts(
        it.Contains,
        "Thank you"
    )