from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProdutosPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def selecionar_filtro(self, valor):
        select = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container"))
        )
        for option in select.find_elements(By.TAG_NAME, "option"):
            if option.get_attribute("value") == valor:
                option.click()
                break

    def precos_listados(self):
        elementos = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        return [float(e.text.replace("$", "")) for e in elementos]

    def nomes_listados(self):
        elementos = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [e.text for e in elementos]

    def adicionar_primeiro_produto(self):
        botao = self.wait.until(
            EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        self.driver.execute_script("arguments[0].click();", botao)

    def contador_carrinho(self):
        badges = self.driver.find_elements(By.CSS_SELECTOR, ".shopping_cart_badge")
        return int(badges[0].text) if badges else 0

    def ir_para_carrinho(self):
        link = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".shopping_cart_link"))
        )
        self.driver.execute_script("arguments[0].click();", link)