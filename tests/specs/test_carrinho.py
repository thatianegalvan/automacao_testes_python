from guara.application import Application
from guara import it
import pytest
from tests.transactions.login_transaction import (LoginTransaction)
from tests.transactions.add_to_cart_transaction import ( AddToCartTransaction)
from tests.transactions.remove_from_cart_transaction import (RemoveFromCartTransaction)

@pytest.mark.regression
def test_adicionar_item_ao_carrinho(driver):

    app = Application(driver)

    app.given(
        LoginTransaction,
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
        it.Equals,
        "1"
    )


@pytest.mark.regression
def test_remover_item_do_carrinho(driver):

    app = Application(driver)

    app.given(
        LoginTransaction,
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
        it.Equals,
        "1"
    )

    app.when(
        RemoveFromCartTransaction
    ).asserts(
        it.Equals,
        "0"
    )