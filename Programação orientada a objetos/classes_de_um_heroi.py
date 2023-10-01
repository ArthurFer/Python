# Arthur Fernando - 01/10/23
# Programa para exercitar o conhecimento de classes e objetos criando um herói de forma simplicada
# utilizando métodos e instâncias

# Declaração da classe
class heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

# Método com condicional para pegar o tipo de ataque
    def tipo_ataque(self, saida):
        self.saida = saida
        if self.tipo == "mago":
            self.saida = "magia"
        elif self.tipo == "guerreiro":
            self.saida = "espada"
        elif self.tipo == "monge":
            self.saida = "artes marciais"
        elif self.tipo == "ninja":
            self.saida = "shuriken"
        return self.saida

# Método para atacar
    def atacar(self,saida):
        print(f"o {self.tipo} atacou usando {self.tipo_ataque(saida)}")

# Instanciando o objeto de forma direta
heroi1 = heroi("Perseu", 28, "monge")
heroi2 = heroi("Ifrit", 30, "ninja")

# Chamada dos objetos
print(f"O herói {heroi1.nome}, {heroi1.idade} anos de idade, é do tipo {heroi1.tipo}")
print("Inimigo encontrado, atacadando...")
heroi1.atacar(heroi1.tipo)
print("\n")
print("---------------------------------------")
print("\n")

print(f"O herói {heroi2.nome}, {heroi2.idade} anos de idade, é do tipo {heroi2.tipo}")
print("Inimigo encontrado, atacadando...")
heroi2.atacar(heroi2.tipo)