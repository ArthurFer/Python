#Declaração de listas
frutas = ["Maçã","Banana","Goiaba","Manga"]

frutas.insert(3, "Pêra") #inserindo um elemento na lista com função insert

frutas.remove("Banana") #remove um elemento da lista

for fruta in frutas:
    print(fruta)

print("--------------------------\n\n")

#Acesso a elementos da lista
frutas[0] #Maçã
frutas[-1] #Goiaba

#Impressão do índice com função enumerate
for index, fruta in enumerate(frutas):
    print(f"{index}: {fruta}")


#Declaração de matrizes em python
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

#Acessando os elementos da matriz
print("---------------------------\n\n")
print(matriz[0]) #Impressão da linha 0
print(matriz[0][0]) #Impressão do elemento da linha 0, coluna 0
print(matriz[0][-1]) #Impressão do elemento da linha zero, última coluna
print(matriz[-1][-1]) #Impressão do elemento da ultima linha e ultima coluna

#Fatiamento da lista
lista = ["p", "Y", "t", "h", "o", "n"]
print(lista[2:]) #Impressão dos elementos da posição dois até o final
print(lista[:2]) #Impressão dos elementos de 0 até 2 -1
print(lista[1:3]) #Impressão dos elementos da posição 1 até 3-1
print(lista[0:3:2]) #Impressão dos elementos da posição 0 até 3-1 de 2 em 2
print(lista[::]) #Imprime toda a lista pois não foi passado parametros
print(lista[::-1]) #Imprime toda a lista de trás para a frente pois o step é -1


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


