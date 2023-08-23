from time import sleep
lista_filmes = list()

tempo = 60
cont = 0

while tempo > 0:
    nome = input("Introduza o nome do filme: ")
    classificacao = int(input("Introduza a classificação do filme: "))
    filme = dict(nome=nome, classificacao=classificacao)
    lista_filmes.append(filme)
    #sleep(1)
    tempo -= 1
    cont += 1

    if cont >= 5:
        break


for f in lista_filmes:
    if f.get("classificacao") <= 16:
        print(f)

print(lista_filmes[::-1])
