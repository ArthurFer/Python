# Programa Calculadora de partidas rankeadas escrito em python para desafio da DIO
# Programador: Arthur Fernando

def calculadora_rankeada (vitorias, derrotas):
    return vitorias - derrotas

instrucao_parada = True

while instrucao_parada:
    vitorias = int(input("Digite a quantidade de vitorias: "))
    derrotas = int(input("Digite a quantidade de derrotas: "))
    saldo_vitorias = calculadora_rankeada(vitorias, derrotas)
    nivel = ""

    if saldo_vitorias <= 10:
        nivel = "Ferro"
        print(f"O Herói tem de saldo {saldo_vitorias} está no nível de {nivel}")
    elif saldo_vitorias >= 11 and saldo_vitorias <= 20:
        nivel = "Bronze"
        print(f"O Herói tem de saldo {saldo_vitorias} está no nível de {nivel}")
    elif saldo_vitorias >= 21 and saldo_vitorias <= 50:
        nivel = "Prata"
        print(f"O Herói tem de saldo {saldo_vitorias} está no nível de {nivel}")
    elif saldo_vitorias >= 51 and saldo_vitorias <= 80:
        nivel = "Ouro"
        print(f"O Herói tem de saldo {saldo_vitorias} está no nível de {nivel}")
    elif saldo_vitorias >= 81 and saldo_vitorias <= 90:
        nivel = "Diamante"
        print(f"O Herói tem de saldo {saldo_vitorias} está no nível de {nivel}")
    elif saldo_vitorias >= 91 and saldo_vitorias <= 100:
        nivel = "Lendario"
        print(f"O Herói tem de saldo {saldo_vitorias} está no nível de {nivel}")
    elif saldo_vitorias <= 101:
        nivel = "Imortal"
        print(f"O Herói tem de saldo {saldo_vitorias} está no nível de {nivel}")


    sair = input("Deseja continuar? sim (s), não (n): ")
    if sair != "s":
        instrucao_parada = False
