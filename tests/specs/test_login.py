from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from tests.fixtures.driver import driver

def test_login_com_sucesso(driver):

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "inventory.html" in driver.current_url


def test_login_invalido(driver):

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("usuario_invalido")
    driver.find_element(By.ID, "password").send_keys("senha_invalida")
    driver.find_element(By.ID, "login-button").click()

    mensagem_erro = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "h3[data-test='error']")
        )
    )

    mensagem_esperada = (
        "Epic sadface: Username and password do not match any user in this service"
    )

    assert mensagem_erro.text == mensagem_esperada