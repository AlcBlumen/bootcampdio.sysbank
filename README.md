Sistema Bancário Simples - SysBank
Este projeto faz parte da avaliação parcial do curso de Engenharia de Dados em Python e implementa um sistema bancário básico que realiza operações de depósito, saque e extrato.

Funcionalidades Principais
1. Depósito
Realiza depósitos de valores positivos, que são registrados e adicionados ao saldo.
2. Saque
Permite até 3 saques diários, com um limite máximo de R$ 500,00 por saque.
Verifica se há saldo suficiente e se o limite de saques não foi excedido antes de completar a transação.
3. Extrato
Lista todos os depósitos e saques realizados, além do saldo atual.
Caso não haja transações, exibe a mensagem "Não foram realizadas movimentações".
4. Saldo
Exibe o saldo atual da conta de forma rápida e clara.
Regras do Sistema
Depósitos: Apenas valores positivos são permitidos.
Saques: Máximo de 3 saques diários, com limite de R$ 500,00 por saque.
Limite de saque e saldo: O sistema informará quando o saldo for insuficiente ou o limite de saques for atingido.
Requisitos
Python 3.6 ou superior.
Instruções de Execução
Clone o repositório:

bash
Copiar código
git clone https://github.com/AlcBlumen/bootcampdio.sysbank.git
Acesse o diretório do projeto:

bash
Copiar código
cd bootcampdio.sysbank
Execute o arquivo sysbank.py:

bash
Copiar código
python sysbank.py
Interaja com o menu de operações:

Depósito
Saque
Extrato
Ver Saldo
Sair
Exemplo de Uso
text
Copiar código
Escolha uma operação:
1 - Depósito
2 - Saque
3 - Extrato
4 - Ver Saldo
5 - Sair
Digite o número da operação: 1
Digite o valor do depósito: R$ 1000.00
Depósito de R$ 1000.00 realizado com sucesso!

Escolha uma operação:
1 - Depósito
2 - Saque
3 - Extrato
4 - Ver Saldo
5 - Sair
Digite o número da operação: 2
Digite o valor do saque: R$ 300.00
Saque de R$ 300.00 realizado com sucesso!

Escolha uma operação:
1 - Depósito
2 - Saque
3 - Extrato
4 - Ver Saldo
5 - Sair
Digite o número da operação: 3
Extrato:
Depósito 1: R$ 1000.00
Saque 1: R$ 300.00
Saldo atual: R$ 700.00
Melhorias Futuras
Implementação de múltiplos usuários com autenticação de conta e agência.
Persistência de dados utilizando banco de dados para armazenar o histórico de transações.
Automação do reset de saques diários com base no controle de data.
Contribuição
Este projeto foi desenvolvido como parte do curso de Engenharia de Dados em Python. Sugestões e melhorias são bem-vindas!

Licença
Licenciado sob a MIT License.
