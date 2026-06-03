from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def ir_para_checkout(self):
        botao = self.wait.until(
            EC.presence_of_element_located((By.ID, "checkout"))
        )
        self.driver.execute_script("arguments[0].click();", botao)

    def preencher_dados(self, nome, sobrenome, cep):
        self.wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys(nome)
        self.driver.find_element(By.ID, "last-name").send_keys(sobrenome)
        self.driver.find_element(By.ID, "postal-code").send_keys(cep)

    def continuar(self):
        botao = self.driver.find_element(By.ID, "continue")
        self.driver.execute_script("arguments[0].click();", botao)

    def mensagem_de_erro(self):
        erros = self.driver.find_elements(By.CSS_SELECTOR, "[data-test='error']")
        return erros[0].text if erros else None