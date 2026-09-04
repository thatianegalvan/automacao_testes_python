Feature: Checkout

    Scenario: Compra de produto com sucesso
        Given que o usuário está logado
        When o usuário adiciona um produto ao carrinho
        And o usuário acessa o carrinho
        And o usuário inicia o checkout
        And o usuário preenche nome, sobrenome e CEP
        And o usuário finaliza a compra
        Then uma mensagem de confirmação deve ser exibida