class SistemaBancario:
    def __init__(self):
        self.saldo = 0.0
        self.depositos = []
        self.saques = []
        self.saques_diarios = 0
        self.limite_saques = 3
        self.limite_saque_valor = 500.0

    def resetar_saques_diarios(self):
        self.saques_diarios = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if self.saques_diarios >= self.limite_saques:
            print("Você atingiu o limite diário de 3 saques.")
            return
        if valor > self.limite_saque_valor:
            print(f"O valor máximo permitido para saque é R$ {self.limite_saque_valor:.2f}.")
            return
        if valor > self.saldo:
            print(f"Saldo insuficiente! Seu saldo atual é R$ {self.saldo:.2f}.")
            return

        # Realizando o saque
        self.saldo -= valor
        self.saques.append(valor)
        self.saques_diarios += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        print(f"Você ainda pode realizar {self.limite_saques - self.saques_diarios} saques hoje.")

    def extrato(self):
        if not self.depositos and not self.saques:
            print("Não foram realizadas movimentações.")
        else:
            print("\nExtrato:")
            for i, deposito in enumerate(self.depositos, start=1):
                print(f"Depósito {i}: R$ {deposito:.2f}")
            for i, saque in enumerate(self.saques, start=1):
                print(f"Saque {i}: R$ {saque:.2f}")
            print(f"\nSaldo atual: R$ {self.saldo:.2f}\n")

    def ver_saldo(self):
        print(f"\nSaldo atual: R$ {self.saldo:.2f}\n")


# Simulação do sistema bancário
banco = SistemaBancario()

while True:
    print("\nEscolha uma operação:")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Extrato")
    print("4 - Ver Saldo")
    print("5 - Sair")
    
    opcao = input("Digite o número da operação: ")

    if opcao == '1':
        valor_deposito = float(input("Digite o valor do depósito: R$ "))
        banco.depositar(valor_deposito)

    elif opcao == '2':
        valor_saque = float(input("Digite o valor do saque: R$ "))
        banco.sacar(valor_saque)

    elif opcao == '3':
        banco.extrato()

    elif opcao == '4':
        banco.ver_saldo()

    elif opcao == '5':
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida! Tente novamente.")
