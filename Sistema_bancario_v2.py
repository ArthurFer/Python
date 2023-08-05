#Sistema bancário v2
#Desenvolvedor: Arthur Fernando
import textwrap

def depositar(saldo, valor_deposito, extrato, /):
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito: .2f}\n"
    else:
        print("O valor informado é inválido, somente valores positivos são permitidos")
    return (saldo, extrato)


def saque(*,saldo, valor_saque, extrato, limite, numero_saques, limite_saques):
    if (numero_saques < limite_saques):
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
        print ("\n\n LIMITE DIARIO DE SAQUE EXCEDIDO \n\n")
    return (saldo, extrato)

def exibir_extrato(saldo, /, *, extrato):
    print("\n------------------ Extrato ------------------")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo: .2f}")
    print("---------------------------------------------")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, numero - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n Usuário não encontrado, fluxo de criação de conta encerrado!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    menu = """
    [d] \tDepositar
    [s] \tSacar
    [e] \tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário 
    [q] Sair

    Escolha a opção desejada
    ->
    """

    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    valor_saque = 0
    valor_deposito = 0
    usuarios = []
    contas = []

    while True:

        opcao = input(menu)

        if opcao == "d":
            print("Depósito")
            valor_deposito =  float(input("Insira valor a ser depositado: "))
            saldo, extrato = depositar(saldo, valor_deposito,extrato)
        
        elif opcao == "s":
            print("Sacar")
            valor_saque = float(input("Informe o valor que deseja sacar: "))        
            saldo, extrato = saque(saldo = saldo, valor_saque= valor_saque, extrato= extrato, limite= limite, numero_saques= numero_saques, limite_saques= LIMITE_SAQUES )
            numero_saques += 1       

        elif opcao == "e":
            exibir_extrato(saldo, extrato= extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()