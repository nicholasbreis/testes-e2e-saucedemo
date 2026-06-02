from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.saucedemo.com"

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir(self):
        self.driver.get(URL)

    def preencher_usuario(self, usuario):
        self.driver.find_element(By.ID, "user-name").clear()
        self.driver.find_element(By.ID, "user-name").send_keys(usuario)

    def preencher_senha(self, senha):
        self.driver.find_element(By.ID, "password").clear()
        self.driver.find_element(By.ID, "password").send_keys(senha)

    def clicar_login(self):
        self.driver.find_element(By.ID, "login-button").click()

    def fazer_login(self, usuario, senha):
        self.preencher_usuario(usuario)
        self.preencher_senha(senha)
        self.clicar_login()

    def mensagem_de_erro(self):
        erros = self.driver.find_elements(By.CSS_SELECTOR, "[data-test='error']")
        return erros[0].text if erros else None

    def esta_na_pagina_de_produtos(self):
        return "inventory" in self.driver.current_url