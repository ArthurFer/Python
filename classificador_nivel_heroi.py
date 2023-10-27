# Programa classificador de nível de herói escrito em python para desafio da DIO
# Programador: Arthur Fernando

# Inicializa uma variável para controlar a instrução de parada
instrucao_parada = True

# Inicia um loop que permite ao usuário inserir informações sobre um herói
while instrucao_parada:
    # Solicita o nome do herói ao usuário
    nome = input("Digite o nome do herói: ")
    
    # Solicita a quantidade de XP do herói ao usuário e converte para um número inteiro
    qtd_xp = int(input("Digite a quantidade de XP: "))
    
    # Inicializa uma variável 'nivel' para armazenar o nível do herói
    nivel = ""
    
    # Classifica o nível do herói com base na quantidade de XP
    if qtd_xp <= 1000:
        nivel = "Ferro"
    elif qtd_xp >= 1001 and qtd_xp <= 2000:
        nivel = "Bronze"
    elif qtd_xp >= 2001 and qtd_xp <= 5000:
        nivel = "Prata"
    elif qtd_xp >= 5001 and qtd_xp <= 7000:
        nivel = "Ouro"
    elif qtd_xp >= 7001 and qtd_xp <= 8000:
        nivel = "Platina Diamante"
    elif qtd_xp >= 8001 and qtd_xp <= 9000:
        nivel = "Ascendente"
    elif qtd_xp >= 9001 and qtd_xp <= 10000:
        nivel = "Imortal"
    elif qtd_xp >= 10001:
        nivel = "Radiante"
    
    # Exibe o resultado com o nome do herói e o nível alcançado
    print(f"O Herói de nome {nome} está no nível de {nivel}")
    
    # Solicita ao usuário se deseja continuar inserindo heróis
    sair = input("Deseja continuar? sim (s), não (n): ")
    if sair != "s":
        instrucao_parada = False
