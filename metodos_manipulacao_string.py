curso = "PyThoN"

#Converte todos os caracteres para maíusculo
print(curso.upper())

#Converte todos os caracteres para minúsculo
print(curso.lower())

#Deixa a primeira letra maiúscula e o restante minúsculo
print(curso.title())

palavra = "     Exemplo "

#Remove os espaços em branco da esquerda e da direita
print(palavra.strip())

#Remove os espaço em branco da esquerda
print(palavra.lstrip())

#Remove os espaço em branco da direita
print(palavra.rstrip())

#Centraliza a string e define tamanho podendo concatenar caracter passado no argumento
print(curso.center(12, "~"))

#Junção que insere 
print(".".join(curso))
