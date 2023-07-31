#Adicionando novos valores a uma lista com função append
numeros = [0, 1, 5, 30, 21, 59, 2, 9, 65, 34]
pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)


print(pares)
print(impares)