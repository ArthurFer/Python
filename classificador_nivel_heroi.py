# Programa classificador de nível de herói escrito em python para desafio da DIO
# Programador: Arthur Fernando


instrucao_parada = True

while instrucao_parada:
    nome = input("Digite o nome do herói: ")
    qtd_xp = int(input("Digite a quantidade de xp: "))
    nivel = ""

    if qtd_xp <= 1000:
        nivel = "Ferro"
        print(f"O Herói de nome {nome} está no nível de {nivel}")
    elif qtd_xp >= 1001 and qtd_xp <= 2000:
        nivel = "Bronze"
        print(f"O Herói de nome {nome} está no nível de {nivel}")
    elif qtd_xp >= 2001 and qtd_xp <= 5000:
        nivel = "Prata"
        print(f"O Herói de nome {nome} está no nível de {nivel}")
    elif qtd_xp >= 5001 and qtd_xp <= 7000:
        nivel = "Ouro"
        print(f"O Herói de nome {nome} está no nível de {nivel}")
    elif qtd_xp >= 7001 and qtd_xp <= 8000:
        nivel = "Platina Diamante"
        print(f"O Herói de nome {nome} está no nível de {nivel}")
    elif qtd_xp >= 8001 and qtd_xp <= 9000:
        nivel = "Ascendente"
        print(f"O Herói de nome {nome} está no nível de {nivel}")
    elif qtd_xp >= 9001 and qtd_xp <= 10000:
        nivel = "Imortal"
        print(f"O Herói de nome {nome} está no nível de {nivel}")
    elif qtd_xp >= 10001:
        nivel = "Radiante"
        print(f"O Herói de nome {nome} está no nível de {nivel}")

    sair = input("Deseja continuar? sim (s), não (n): ")
    if sair != "s":
        instrucao_parada = False
