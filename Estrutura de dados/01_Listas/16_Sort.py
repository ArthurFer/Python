linguagens = ["python", "C", "C++", "java", "angular"]
linguagens.sort() #Ordena a lista em ordem alfabética
print("Ordenado em ordem alfabética: ", linguagens)


linguagens = ["python", "C", "C++", "java", "angular"]
linguagens.sort(reverse=True) #Ordena a lista em ordem decrescente
print("Ordenado em ordem decrescente: ", linguagens)

linguagens = ["python", "C", "C++", "java", "angular"]
linguagens.sort(key= lambda x: len(x))
print("Ordenado do menor tamanho para o maior: ", linguagens)

linguagens = ["python", "C", "C++", "java", "angular"]
linguagens.sort(key= lambda x: len(x), reverse=True)
print("Ordenado do maior tamanho para o menor: ", linguagens)

