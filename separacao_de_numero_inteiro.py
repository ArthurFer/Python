# Entrada de uma string com números
n = input("Digite um número inteiro com mais de 3 digitos: ")

# Slice da string para inverter ordem
y = n[::-1]

# Inserção de um espaço em branco com o método join
k = " ".join(y)
print(k)
