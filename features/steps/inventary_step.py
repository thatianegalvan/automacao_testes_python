from behave import given, when, then

@when('o usuário seleciona a ordenação "{opcao}"')
def step_select_sorting(context, opcao):
    # Lógica de seleção do filtro
    pass

@then('o primeiro produto exibido deve ser o "{nome_produto}"')
def step_validate_first_product_name(context, nome_produto):
    # Lógica de validação do nome do produto
    pass

@then('o valor do primeiro produto deve ser "{preco}"')
def step_validate_first_product_price(context, preco):
    # Lógica de validação do preço
    pass

@when('o usuário abre o menu lateral e clica em "{opcao_menu}"')
def step_click_sidebar_option(context, opcao_menu):
    # Lógica do menu lateral
    pass

@then('o contador do carrinho não deve ser exibido')
def step_validate_cart_badge_hidden(context):
    # Lógica para checar que o badge do carrinho sumiu
    pass