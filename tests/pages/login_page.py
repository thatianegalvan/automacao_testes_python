from selenium.webdriver.common.by import By

#Ainda testei
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def acessar(self):
            self.driver.get("https://sua-url.com/login")

    def preencher_usuario(self, usuario):
        self.driver.find_element(By.ID, "username").send_keys(usuario)


    def preencher_senha(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.ID, "login-button").click()

    