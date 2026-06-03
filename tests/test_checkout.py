from pages.produtos_page import ProdutosPage
from pages.checkout_page import CheckoutPage


def test_checkout_sem_dados_exibe_erro(driver_logado):
    """Cenário negativo: tentar continuar o checkout sem preencher dados deve exibir erro."""
    produtos = ProdutosPage(driver_logado)
    checkout = CheckoutPage(driver_logado)

    produtos.adicionar_primeiro_produto()
    produtos.ir_para_carrinho()
    checkout.ir_para_checkout()
    checkout.continuar()  # tenta continuar sem preencher nada

    erro = checkout.mensagem_de_erro()
    assert erro is not None, "Deveria exibir mensagem de erro ao continuar sem dados"
    assert "first name" in erro.lower(), \
        f"Mensagem de erro inesperada: {erro}"