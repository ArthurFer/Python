def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def potencia(a, b):
    return a ** b

def multiplicacao(a, b):
    return a * b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")

a = int(input("Digite o primeiro número: "))
b = int(input("\nDigite o segundo número: "))

exibir_resultado(a, b, somar)  # O resultado da operação 10 + 10 = 20
exibir_resultado(10, 2, subtrair)  # O resultado da operação 10 + 10 = 20
exibir_resultado(10, 2, potencia)  # O resultado da operação 10 + 10 = 20
exibir_resultado(10, 2, multiplicacao)  # O resultado da operação 10 + 10 = 20