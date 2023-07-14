def sacar (valor):
    saldo = 500

    if (saldo >= valor):
        print("Operação efetuada com sucesso")
        print("Retire o dinheiro")
    else:
        print("Saldo insuficiente")


print("Caixa Eletronico\n\n")
saque = input("Informe o valor que deseja sacar: ")
saque = float(saque)
sacar(saque)


