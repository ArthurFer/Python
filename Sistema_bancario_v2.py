# Sistema bancário v2
# Refatoração do Sistema bancário v1 para um modelo funcional, Este código é um sistema bancário mais complexo com suporte para múltiplos usuários e contas. 
# Ele permite a criação de usuários, a criação de contas associadas a usuários, a realização de depósitos, saques e exibição de extratos. 
# Desenvolvedor: Arthur Fernando

# Importa o módulo 'textwrap' para formatar a exibição de informações de conta
import textwrap

# Define uma função 'depositar' que lida com operações de depósito
def depositar(saldo, valor_deposito, extrato, /):
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito: .2f}\n"
    else:
        print("O valor informado é inválido, somente valores positivos são permitidos")
    return (saldo, extrato)

# Define uma função 'saque' que lida com operações de saque
def saque(*, saldo, valor_saque, extrato, limite, numero_saques, limite_saques):
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

# Define uma função 'exibir_extrato' para mostrar as informações do extrato da conta
def exibir_extrato(saldo, /, *, extrato):
    print("\n------------------ Extrato ------------------")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo: .2f}")
    print("---------------------------------------------")

# Define uma função 'criar_usuario' que permite criar um novo usuário
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

# Define uma função 'filtrar_usuario' que busca um usuário por CPF
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

# Define uma função 'criar_conta' que permite criar uma nova conta associada a um usuário
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n Usuário não encontrado, fluxo de criação de conta encerrado!")

# Define uma função 'listar_contas' que exibe informações de todas as contas
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

# Função principal do programa
def main():
    # Menu de opções para o usuário
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

    # Variáveis e constantes
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    valor_saque = 0
    valor_deposito = 0
    usuarios = []  # Armazena informações de usuários
    contas = []    # Armazena informações de contas

    while True:
        # Solicita ao usuário que escolha uma opção do menu
        opcao = input(menu)

        if opcao == "d":
            print("Depósito")
            valor_deposito =  float(input("Insira valor a ser depositado: "))
            saldo, extrato = depositar(saldo, valor_deposito, extrato)

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

# Chama a função principal para iniciar o programa
main()
