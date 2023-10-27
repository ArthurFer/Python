# Sistema bancário simples que permite ao usuário realizar depósitos, saques e verificar o extrato de sua conta
# Desenvolvedor: Arthur Fernando

# Menu de opções para o usuário
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Escolha a opção desejada
->
"""

# Inicialização de variáveis de controle
saldo = 0
limite = 500
extrato = ""  # Armazena o extrato das operações
numero_saques = 0
LIMITE_SAQUES = 3  # Limite máximo de saques diários

# Loop principal do programa
while True:
    # Solicita ao usuário que escolha uma opção do menu
    opcao = input(menu)

    if opcao == "d":
        # Opção de depósito
        print("Depósito")
        valor_deposito =  float(input("Insira valor a ser depositado: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito: .2f}\n"  # Atualiza o extrato com a operação de depósito
        else:
            print("O valor informado é inválido, somente valores positivos são permitidos")

    elif opcao == "s":
        # Opção de saque
        if (numero_saques < LIMITE_SAQUES):
            print("Sacar")
            valor_saque = float(input("Informe o valor que deseja sacar: "))
            if valor_saque > 0:
                if (valor_saque <= limite) and (valor_saque <= saldo):
                    saldo = saldo - valor_saque
                    print("Saque realizado com sucesso.")
                    numero_saques += 1
                    extrato += f"Saque: -R$ {valor_saque: .2f}\n"  # Atualiza o extrato com a operação de saque
                elif (valor_saque > limite):
                    print ("Limite por saque R$ 500.00")
                else:
                    print ("Saldo insuficiente para realização de saque.")
            else:
                print("Somente valores positivos são aceitos.")
        else:
            print ("Limite diário de saque excedido.")
    
    elif opcao == "e":
        # Opção de extrato
        print("\n------------------ Extrato ------------------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo: .2f}")
        print("---------------------------------------------")

    elif opcao == "q":
        # Opção de sair do programa
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
