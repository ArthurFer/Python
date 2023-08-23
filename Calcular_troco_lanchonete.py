valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())


valor_total_pedido = (valorHamburguer * quantidadeHamburguer) + (valorBebida * quantidadeBebida)

troco = valorPago - valor_total_pedido

print(f"O preço final do pedido é R$ {valor_total_pedido: .2f}. Seu troco é R$ {troco: .2f}.")

valorPedido = int(input())

if valorPedido >= 50:
    print(f"Parabens, você ganhou uma sobremesa gratis!")
else:
    print(f"Que pena, você não ganhou nenhum brinde especial.")