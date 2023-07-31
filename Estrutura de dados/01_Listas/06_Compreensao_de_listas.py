#Adicionando novos valores a uma lista forma comprimida
numeros = [0, 1, 5, 30, 21, 59, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print (sorted(pares)) #função sorted organiza os valores em ordem crescente
print (sorted(impares))

quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2) #modificando elementos da lista
    
print(quadrado)

quadrado = [numero**2 for numero in numeros] #modificando elementos de forma comprimida
print(quadrado)