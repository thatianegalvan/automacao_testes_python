from tests.pages.login_page import LoginPage

class LoginTransation:
    def __init__(self, driver):
        self.login_page = LoginPage(driver)

    def realizar_login(self, usuario, senha):
        self.login_page.acessar()
        self.login_page.preencher_usuario(usuario)
        self.login_page.preencher_senha(senha)
        self.login_page.click_login_button()