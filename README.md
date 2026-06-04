# Testes E2E | SauceDemo

Projeto de testes End-to-End desenvolvido com **Selenium** e **Pytest** para fins acadêmicos

## Sistema escolhido

**SauceDemo** (https://www.saucedemo.com)

O SauceDemo é uma aplicação web de e-commerce criada pela Sauce Labs especificamente para fins de demonstração e testes automatizados. O sistema simula uma loja virtual completa com fluxos de autenticação, listagem de produtos, carrinho de compras e checkout.

Foi escolhido por permitir a execução de testes E2E reais sem restrições de acesso, sem bloqueios de automação e com fluxos ricos de interação de usuário.

## Funcionalidades testadas

| Teste | Tipo | Descrição |
|---|---|---|
| Login com credenciais válidas | Positivo | Verifica se o usuário é redirecionado para a página de produtos |
| Login com usuário bloqueado | Negativo | Verifica se a mensagem de erro correta é exibida |
| Login com campos vazios | Negativo | Verifica se a validação de campos obrigatórios funciona |
| Filtro de produtos por menor preço | Positivo | Verifica se os produtos são ordenados corretamente |
| Adicionar produto ao carrinho | Positivo | Verifica se o contador do carrinho é atualizado |
| Checkout sem dados preenchidos | Negativo | Verifica se a validação dos campos do formulário funciona |

## Padrões utilizados

- **Page Objects:** cada página do sistema é representada por uma classe em `pages/`. Os testes não interagem diretamente com o Selenium, toda a lógica de localização de elementos fica encapsulada nas classes de página.
- **Fixtures:** o `conftest.py` define duas fixtures reutilizáveis: `driver` (Chrome headless inicializado) e `driver_logado` (driver já autenticado, usado nos testes que dependem de login).
- **Esperas explícitas:** uso de `WebDriverWait` com `expected_conditions` para aguardar elementos antes de interagir, evitando falhas por timing.
- **Cliques via JavaScript:** o SauceDemo é construído em React e em modo headless os cliques nativos do Selenium não disparam os eventos corretamente. Por isso os cliques são executados via `execute_script`, o que é uma prática válida e documentada para aplicações React.

## Pré-requisitos

- Python 3.10+
- Google Chrome instalado
- pip

## Instalação

```bash
# Clone o repositório
git clone https://github.com/nicholasbreis/testes-e2e-saucedemo.git
cd testes-e2e-saucedemo

# Instale as dependências
pip install -r requirements.txt
```

> O `webdriver-manager` baixa automaticamente o ChromeDriver compatível com a versão do Chrome instalada. Não é necessário instalar o ChromeDriver manualmente.

## Como executar

```bash
# Executar todos os testes
pytest tests/ -v

# Executar com relatório HTML
pytest tests/ -v --html=relatorio.html --self-contained-html

# Executar apenas os testes de login
pytest tests/test_login.py -v

# Executar apenas os testes de produtos
pytest tests/test_produtos.py -v

# Executar apenas os testes de checkout
pytest tests/test_checkout.py -v
```

## Credenciais utilizadas nos testes

| Usuário | Senha | Comportamento |
|---|---|---|
| `standard_user` | `secret_sauce` | Login válido |
| `locked_out_user` | `secret_sauce` | Usuário bloqueado |

## Resultado esperado
tests/test_checkout.py::test_checkout_sem_dados_exibe_erro PASSED \
tests/test_login.py::test_login_valido_redireciona_para_produtos PASSED\
tests/test_login.py::test_login_usuario_bloqueado_exibe_erro PASSED\
tests/test_login.py::test_login_campos_vazios_exibe_erro PASSED\
tests/test_produtos.py::test_filtro_menor_preco_ordena_corretamente PASSED\
tests/test_produtos.py::test_adicionar_produto_atualiza_carrinho PASSED\
6 passed in ~40s

## Observações

- Os testes rodam em modo **headless** (sem abrir janela do navegador), adequado para ambientes de CI/CD como o GitHub Codespaces.
- Nenhum teste realiza compras reais, cria cadastros abusivos ou sobrecarrega o sistema. Todos os fluxos são seguros e respeitam as diretrizes de uso da aplicação.
