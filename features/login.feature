Feature: Login
  Scenario: Login válido
    Given que o usuário acessa a página de login
    When ele realiza login com usuário válido
    Then ele deve ser redirecionado para a página de inventário

  Scenario: Login inválido
    Given que o usuário acessa a página de login
    When ele realiza login com credenciais inválidas
    Then ele deve ver uma mensagem de erro