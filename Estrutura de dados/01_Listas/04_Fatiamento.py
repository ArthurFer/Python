#Fatiamento da lista
lista = ["p", "Y", "t", "h", "o", "n"]
print(lista[2:]) #Impressão dos elementos da posição dois até o final
print(lista[:2]) #Impressão dos elementos de 0 até 2 -1
print(lista[1:3]) #Impressão dos elementos da posição 1 até 3-1
print(lista[0:3:2]) #Impressão dos elementos da posição 0 até 3-1 de 2 em 2
print(lista[::]) #Imprime toda a lista pois não foi passado parametros
print(lista[::-1]) #Imprime toda a lista de trás para a frente pois o step é -1