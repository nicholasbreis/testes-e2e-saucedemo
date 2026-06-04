from pages.produtos_page import ProdutosPage


def test_filtro_menor_preco_ordena_corretamente(driver_logado):
    page = ProdutosPage(driver_logado)
    page.selecionar_filtro("lohi")

    precos = page.precos_listados()
    assert precos == sorted(precos), \
        f"Preços não estão em ordem crescente: {precos}"


def test_adicionar_produto_atualiza_carrinho(driver_logado):
    page = ProdutosPage(driver_logado)

    badges_antes = driver_logado.find_elements("css selector", ".shopping_cart_badge")
    assert len(badges_antes) == 0, "Carrinho deveria estar vazio inicialmente"

    page.adicionar_primeiro_produto()

    assert page.contador_carrinho() == 1, \
        "Contador do carrinho deveria ser 1 após adicionar produto"