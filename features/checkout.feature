Feature: Checkout

    Background: Usuário autenticado
        Given que o usuário está logado

    Scenario: Compra de produto com sucesso
        Given o usuário adiciona o produto "Sauce Labs Bike Light" ao carrinho
        When o usuário acessa o carrinho
        Then o produto "Sauce Labs Bike Light" deve estar presente no carrinho
        When o usuário inicia o checkout
        Then o usuário preenche nome "Teste", sobrenome "Teste" e CEP "12345"
        When o usuário finaliza a compra
        Then uma mensagem de confirmação deve ser exibida