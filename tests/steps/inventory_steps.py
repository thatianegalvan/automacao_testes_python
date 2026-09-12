from behave import given, when, then

from tests.pages.inventory_page import InventoryPage

@when('o usuário seleciona a ordenação "{opcao}"')
def step_select_sorting(context, opcao):
    context.inventory_page = InventoryPage(context.driver)
    context.inventory_page.clicar_filtro()
    context.inventory_page.select_sorting(opcao)

@then('o primeiro produto exibido deve ser o "{nome_produto}"')
def validate_first_product_name(context, nome_produto):
    context.inventory_page = InventoryPage(context.driver)
    context.inventory_page.show_product_by_name(nome_produto)
    

@then('o valor do primeiro produto deve ser "{preco}"')
def validate_first_product_price(context, preco):
    context.inventory_page = InventoryPage(context.driver)
    context.inventory_page.show_product_by_price(preco)

    
@given('o usuário adiciona o produto "{nome_produto}" ao carrinho')
def step_add_product_to_cart(context, nome_produto):
    context.inventory_page = InventoryPage(context.driver)
    context.inventory_page.add_product_by_name(nome_produto) 
    print(f"Produto '{nome_produto}' adicionado ao carrinho com sucesso.")   

@when('o usuário abre o menu lateral e clica em Reset App State')
def click_sidebar_option(context):
    context.inventory_page = InventoryPage(context.driver)
    context.inventory_page.open_sidebar_menu()
    context.inventory_page.click_sidebar_option()


@when('o usuário abre o menu lateral e clica em All Items')
def click_sidebar_option(context):
    context.inventory_page = InventoryPage(context.driver)
    context.inventory_page.open_sidebar_menu()
    context.inventory_page.click_all_items_option()    

@then('o contador do carrinho não deve ser exibido')
def validate_cart_badge_hidden(context):
    context.inventory_page = InventoryPage(context.driver)
    context.inventory_page.is_cart_empty()


@then('o carrinho deve estar vazio')
def validate_cart_empty(context):
    context.inventory_page = InventoryPage(context.driver)
    context.inventory_page.remove_product()

    assert context.cart_page.is_cart_empty(), "O carrinho não está vazio após a remoção do produto."

    
   