# Arthur Fernando
# 11/09/2023
# O objetivo deste programa é a declaração de classes, objetos, métodos e instâncias como prática
# da teoria aprendida sobre orientação a objetos com Python

# Declaração da classe Bicicleta com seus atributos e métodos, instânciados com o self
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmm...")

# Método para representação da classe
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

# Atribuição de valores ao objeto e chamada dos métodos de forma direta
b1 = Bicicleta("vermelha", "caloi", 2020, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

# Atribuição de valores através do input do usuário
b2 = Bicicleta(input("Cor: "), input("modelo: "), input("ano: "), input("valor: "))
print(b2)
