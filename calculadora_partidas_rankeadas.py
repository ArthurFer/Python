# Programa Calculadora que permite ao usuário inserir informações sobre partidas ranqueadas, como o número de vitórias e derrotas, 
# e calcula o saldo de vitórias e derrotas. Com base nesse saldo, o programa classifica o nível do jogador. 
# O programa continua rodando até que o usuário escolha a opção de sair.

# Programador: Arthur Fernando

# Define uma função chamada 'calculadora_rankeada' que calcula o saldo de vitórias e derrotas
def calculadora_rankeada(vitorias, derrotas):
    return vitorias - derrotas

# Inicializa uma variável para controlar a instrução de parada
instrucao_parada = True

# Inicia um loop que permite ao usuário inserir informações sobre partidas ranqueadas
while instrucao_parada:
    # Solicita ao usuário o número de vitórias e o número de derrotas
    vitorias = int(input("Digite a quantidade de vitórias: "))
    derrotas = int(input("Digite a quantidade de derrotas: "))
    
    # Calcula o saldo de vitórias e derrotas usando a função definida
    saldo_vitorias = calculadora_rankeada(vitorias, derrotas)
    nivel = ""

    # Classifica o nível do herói com base no saldo de vitórias e derrotas
    if saldo_vitorias <= 10:
        nivel = "Ferro"
    elif saldo_vitorias >= 11 and saldo_vitorias <= 20:
        nivel = "Bronze"
    elif saldo_vitorias >= 21 and saldo_vitorias <= 50:
        nivel = "Prata"
    elif saldo_vitorias >= 51 and saldo_vitorias <= 80:
        nivel = "Ouro"
    elif saldo_vitorias >= 81 and saldo_vitorias <= 90:
        nivel = "Diamante"
    elif saldo_vitorias >= 91 and saldo_vitorias <= 100:
        nivel = "Lendário"
    elif saldo_vitorias >= 101:
        nivel = "Imortal"
    
    # Exibe o resultado com o saldo de vitórias e derrotas e o nível alcançado
    print(f"O Herói com saldo de {saldo_vitorias} está no nível de {nivel}")

    # Solicita ao usuário se deseja continuar inserindo informações sobre partidas ranqueadas
    sair = input("Deseja continuar? sim (s), não (n): ")
    if sair != "s":
        instrucao_parada = False
