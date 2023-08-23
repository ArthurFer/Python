matriz = []
maior = 0
maior = float(maior)
media = [12]


for i in range(2):
    linha =[]
    for j in range(12):
        list.append(linha, float(input()))
    matriz = matriz + [linha]


for j in range(12):
    print(f"Temperaturas - T1: {matriz[0][j]} | T2 {matriz[1][j]}")
    print("|-------------------------------|")

for i in range(2):
    for j in range(12):
        media[j] = (matriz[0][j] + matriz[1][j])/2

for j in range(12):
    print(f"Media= {media[j]}")
    print("|-------------------------------|")


