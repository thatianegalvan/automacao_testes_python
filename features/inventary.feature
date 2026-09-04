Feature: Inventário e Filtros

    Background: Usuário autenticado
        Given que o usuário está logado

    Scenario: Ordenar produtos por menor preço
        When o usuário seleciona a ordenação "Price (low to high)"
        Then o primeiro produto exibido deve ser o "Sauce Labs Onesie"
        And o valor do primeiro produto deve ser "$7.99"

    Scenario: Limpar estado do aplicativo pelo menu lateral
        Given o usuário adiciona um produto ao carrinho
        When o usuário abre o menu lateral e clica em "Reset App State"
        Then o contador do carrinho não deve ser exibido