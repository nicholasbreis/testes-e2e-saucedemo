from pages.login_page import LoginPage


def test_login_valido_redireciona_para_produtos(driver):
    page = LoginPage(driver)
    page.abrir()
    page.fazer_login("standard_user", "secret_sauce")

    assert page.esta_na_pagina_de_produtos(), \
        "Deveria redirecionar para a página de produtos após login válido"


def test_login_usuario_bloqueado_exibe_erro(driver):
    page = LoginPage(driver)
    page.abrir()
    page.fazer_login("locked_out_user", "secret_sauce")

    erro = page.mensagem_de_erro()
    assert erro is not None, "Deveria exibir mensagem de erro"
    assert "locked out" in erro.lower(), \
        f"Mensagem de erro inesperada: {erro}"


def test_login_campos_vazios_exibe_erro(driver):
    page = LoginPage(driver)
    page.abrir()
    page.clicar_login()

    erro = page.mensagem_de_erro()
    assert erro is not None, "Deveria exibir mensagem de erro para campos vazios"
    assert "username" in erro.lower(), \
        f"Mensagem de erro inesperada: {erro}"