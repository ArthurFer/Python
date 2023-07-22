#Sistema bancário v1
#Desenvolvedor: Arthur Fernando

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Escolha a opção desejada
->
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor_deposito =  float(input("Insira valor a ser depositado: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito: .2f}\n"
        else:
            print("O valor informado é inválido, somente valores positivos são permitidos")
    elif opcao == "s":        
        if (numero_saques < LIMITE_SAQUES):
            print("Sacar")
            valor_saque = float(input("Informe o valor que deseja sacar: "))
            if valor_saque > 0:
                if (valor_saque <= limite) and (valor_saque <= saldo):
                    saldo = saldo - valor_saque
                    print("Saque realizado com sucesso.")
                    numero_saques += 1
                    extrato += f"Saque: -R$ {valor_saque: .2f}\n"
                elif (valor_saque > limite):
                    print ("Limite por saque R$ 500.00")
                else:
                    print ("Saldo insuficiente para realização de saque.")   
            else:
                print("Somente valores positivos são aceitos.") 
        else:
            print ("Limite diário de saque excedido.")
               

    elif opcao == "e":
        print("\n------------------ Extrato ------------------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo: .2f}")
        print("---------------------------------------------")
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
