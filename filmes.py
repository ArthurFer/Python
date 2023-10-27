# Programa que classifica um filme por sua faixa etária

# Importa a função 'sleep' do módulo 'time'
from time import sleep

# Inicializa uma lista vazia chamada 'lista_filmes' para armazenar informações de filmes
lista_filmes = list()

# Inicializa variáveis 'tempo' e 'cont' para controlar o loop e contar filmes inseridos
tempo = 60
cont = 0

# Inicia um loop que permite ao usuário inserir informações sobre filmes
while tempo > 0:
    # Solicita o nome do filme ao usuário
    nome = input("Introduza o nome do filme: ")
    
    # Solicita a classificação do filme (idade recomendada) ao usuário e converte para um número inteiro
    classificacao = int(input("Introduza a classificação do filme: "))
    
    # Cria um dicionário 'filme' com as informações do filme e o adiciona à lista 'lista_filmes'
    filme = dict(nome=nome, classificacao=classificacao)
    lista_filmes.append(filme)
    
    # Decrementa o valor de 'tempo' e incrementa 'cont' para controlar o número de filmes inseridos
    tempo -= 1
    cont += 1
    
    # Se 'cont' for maior ou igual a 5, sai do loop
    if cont >= 5:
        break

# Itera sobre a lista de filmes e imprime aqueles com classificação menor ou igual a 16
for f in lista_filmes:
    if f.get("classificacao") <= 16:
        print(f)

# Imprime a lista de filmes em ordem reversa (do último inserido ao primeiro)
print(lista_filmes[::-1])
