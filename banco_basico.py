menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depositar")
        deposito = float(input("Informe o valor do deposito: "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
        
        else:
            print("Operação invalida, tente novamente!")

    elif opcao == "s":
        print("Saque")
        saque = float(input("Informe o valor do saque: "))
        if saque > 0:
            saldo = saldo - saque
            print(saldo)

        elif LIMITE_SAQUES > 3:
            print("Você já atingiu o limite de saques de hoje")    
    elif opcao == "e":
        print("Extrato")

    elif opcao == "q":
        break

    else:
        print("Operação invalida.")   


