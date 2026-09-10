# 🛠️ Guia de Comandos Úteis - Automação & Git

Este documento reúne os principais comandos utilizados no dia a dia do desenvolvimento, execução de testes automatizados com Behave e controle de versão com Git.


## 1. Execução de Testes (Behave & Python)

### Ativação do Ambiente Virtual

## Ativar o venv no Linux/macOS
source venv/bin/activate

## Executar todas as features do projeto
behave

## Executar apenas uma feature específica
behave features/login.feature
behave features/checkout.feature

# Executar apenas um cenário específico (linha do arquivo)
behave features/login.feature:3

# Executar exibindo prints/logs no terminal em tempo real
behave --no-capture

# Executar uma feature exibindo os logs
behave features/checkout.feature --no-capture

# Controle de versão GIT
# Verificar o status dos arquivos (modificados, não rastreados, etc.)
git status

# Exibir o histórico de commits simplificado
git log --oneline

# Adicionar todos os arquivos modificados para a área de stage
git add .

# Adicionar um arquivo específico
git add features/steps/checkout_steps.py

# Criar um commit com mensagem
git commit -m "feat: ajusta assertions do checkout e adiciona documentação da PoC"

# Enviar as alterações locais para o GitHub/GitLab
git push origin main

# Baixar as últimas atualizações do repositório remoto
git pull origin main

# Desfazer alterações não salvas em um arquivo específico
git checkout -- features/steps/checkout_steps.py

# Criar uma nova branch de funcionalidade
git checkout -b feature/novos-testes-inventario

## Comando uteis do terminal e do Linux

# Exibir árvore de arquivos ignorando o venv e cache
tree -I venv -I __pycache__

# Exibir apenas pastas na árvore
tree -d -I venv -I __pycache__

# Matar processo em execução pelo nome (ex: opencode)
pkill -f opencode

# Matar processo que esteja utilizando uma porta específica (ex: porta 4096)
fuser -k 4096/tcp

## Reiniciar o VS Code 
Use o comando Ctrl + Shift + P no VS Code.
Digite e selecione: Developer: Reload Window (ou simplesmente feche e abra o VS Code).

