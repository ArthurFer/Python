# import sys


# nome_restaurante = str(input())
# tempo_estimado_entrega = int(input())

# print(f"O restaurante {nome_restaurante} entrega em {tempo_estimado_entrega} minutos")


# valorHamburguer = float(input())
# quantidadeHamburguer = int(input())
# valorBebida = float(input())
# quantidadeBebida = int(input())
# valorPago = float(input())


# valor_total_pedido = (valorHamburguer * quantidadeHamburguer) + (valorBebida * quantidadeBebida)

# troco = valorPago - valor_total_pedido 

# print (f"O preço final do pedido é R$ {valor_total_pedido: .2f}. Seu troco é R$ {troco: .2f}.")
       
# valorPedido = int(input())

# if valorPedido >= 50:
#   print(f"Parabens, você ganhou uma sobremesa gratis!")
# else:
#   print(f"Que pena, você não ganhou nenhum brinde especial.") 

# def main():
#     n = int(input())
 
#     total = 0
 
#     for i in range(1, n + 1):
#         pedido = input().split(" ")
#         nome = pedido[0]
#         valor = float(pedido[1])
#         total += valor
 
 
#     cupom = input()

#     if cupom == "10%":
#       total = total * 0.90
#     elif cupom == "20%":
#       total = total * 0.80
 

#     print(f"Valor total: {total: .2f}")
 
 
# if __name__ == "__main__":
#   main()

numPedidos = int(input())
lista_pratos = []

for i in range(1, numPedidos + 1):
    prato = input()
    calorias = int(input())
    ehVegano = False
    condicional_vegano = input()
    
    if condicional_vegano == "s":
      vegano = "(Vegano)"
    else:
      vegano = "(Nao-vegano)"
    lista_pratos.append(f"Pedido {i}: {prato} {vegano} - {calorias} calorias")

for pedidos in lista_pratos:
  print(pedidos)
  print()