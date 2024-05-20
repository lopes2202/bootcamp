opcao = -1

while opcao != 0:
    opcao = int(input('[1] SACAR \n[2] EXTRATO \n[0] SAIR \n'))

    if opcao == 1:
        print("SACANDO")
    elif opcao == 2:
        print("Exibindo o extrato")
else:
    print("Tchau")           