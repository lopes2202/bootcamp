menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

class ContaBancaria:
    LIMITE_SAQUES = 3
    LIMITE_VALOR_SAQUES = 500

    def __init__(self):
        self.saldo = 0
        self.numero_saques = 0
        self.operacoes = []        

    def depositar(self, valor):
        self.saldo += valor
        self.operacoes.append(
            f'R$ +{valor:.2f}'
        )


    def saque(self, valor):

        if self.numero_saques >= self.LIMITE_SAQUES:
            print("Você não pode mais realizar saques hoje")
            return
        elif valor > self.saldo:
            print("Você não tem saldo suficiente")
            return
        elif valor > self.LIMITE_VALOR_SAQUES:
            print(f"O saque não pode ser maior do que o limite de saque de R$ {self.LIMITE_VALOR_SAQUES:.2f}")
            return

        self.saldo = self.saldo - valor
        self.numero_saques += 1
        self.operacoes.append(
            f'R$ -{valor:.2f}'
        )

    def imprimir_extrato(self):
        print("\n================ EXTRATO ================")

        for operacao in self.operacoes:
            print(operacao)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")


    
conta = ContaBancaria()
while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depositar")
        deposito = float(input("Informe o valor do deposito: "))

        if deposito > 0:
            conta.depositar(deposito)
        
        else:
            print("Operação invalida, tente novamente!")

    elif opcao == "s":
        print("Saque")
        saque = float(input("Informe o valor do saque: "))
        
        
        if saque > 0:
            conta.saque(saque)
        else:    
            print("Operação invalida, tente novamente!")

    elif opcao == "e":
        conta.imprimir_extrato()           
    elif opcao == "q":
        break

    else:
        print("Operação invalida.")   


