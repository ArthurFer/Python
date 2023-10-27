# Programa para exercitar o aprendizado do conceito de classes

# Define a classe base "Veiculo"
class Veiculo:
    # O construtor da classe inicializa as propriedades cor, placa e numero_rodas.
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    # Método para ligar o motor do veículo
    def ligar_motor(self):
        print("Ligando o motor...")

    # Método especial __str__ para criar uma representação de string personalizada
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

# Define a classe "Motocicleta", que herda da classe base "Veiculo"
class Motocicleta(Veiculo):
    pass  # Nenhuma alteração ou adição de métodos na classe Motocicleta

# Define a classe "Carro", que também herda da classe base "Veiculo"
class Carro(Veiculo):
    pass  # Nenhuma alteração ou adição de métodos na classe Carro

# Define a classe "Caminhao", que herda da classe base "Veiculo"
class Caminhao(Veiculo):
    # O construtor da classe Caminhao recebe a cor, placa, numero_rodas e carregado como parâmetros.
    def __init__(self, cor, placa, numero_rodas, carregado):
        # Chama o construtor da classe base "Veiculo" usando super() para inicializar cor, placa e numero_rodas.
        super().__init__(cor, placa, numero_rodas)
        # Adiciona a propriedade "carregado" específica para caminhões.
        self.carregado = carregado

    # Método personalizado para verificar se o caminhão está carregado ou não.
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

# Cria instâncias de objetos para cada classe de veículo (Motocicleta, Carro, Caminhao).
moto = Motocicleta("preta", "abc-1234", 2)
moto.ligar_motor()  # Chama o método "ligar_motor" da classe base.

carro = Carro("branco", "kjh-0987", 4)
carro.ligar_motor()

caminhao = Caminhao("amarelo", "oiu-4532", 8, False)
caminhao.ligar_motor()
caminhao.esta_carregado()  # Chama o método personalizado "esta_carregado" para o caminhão.

# Imprime as representações em string dos objetos usando o método especial __str__.
print(caminhao)
print(moto)
print(carro)

