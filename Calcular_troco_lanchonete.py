# Programa que pega as informações sobre os itens do pedido e o valor pago, calcula o valor total do pedido e o troco, 
# e então verifica se o cliente ganhou uma sobremesa grátis com base no valor do pedido.

# Solicita ao usuário o valor do hambúrguer e o converte para um número float
valorHamburguer = float(input()) 

# Solicita ao usuário a quantidade de hambúrgueres desejados e o converte para um número inteiro.
quantidadeHamburguer = int(input())

# Solicita ao usuário o valor da bebida e o converte para um número float
valorBebida = float(input()) 

# Solicita ao usuário a quantidade de bebidas desejadas e o converte para um número inteiro.
quantidadeBebida = int(input()) 

# Solicita ao usuário o valor pago pelo cliente e o converte para um número float.
valorPago = float(input()) 

# Calcula o valor total do pedido somando o valor dos hambúrgueres e o valor das bebidas.
valor_total_pedido = (valorHamburguer * quantidadeHamburguer) + (valorBebida * quantidadeBebida)

# Calcula o troco a ser dado ao cliente, subtraindo o valor total do pedido do valor pago.
troco = valorPago - valor_total_pedido

# Exibe o preço final do pedido e o troco, com formatação para exibir duas casas decimais.
print(f"O preço final do pedido é R$ {valor_total_pedido: .2f}. Seu troco é R$ {troco: .2f}.")

# Solicita ao usuário um valor de pedido.
valorPedido = int(input())

if valorPedido >= 50:
    # Verifica se o valor do pedido é maior ou igual a 50 e, se for verdade, exibe uma mensagem de parabéns com a oferta de uma sobremesa grátis
    print(f"Parabens, você ganhou uma sobremesa gratis!")
else:
    # Se o valor do pedido for menor que 50, exibe uma mensagem informando que o cliente não ganhou nenhum brinde especial.
    print(f"Que pena, você não ganhou nenhum brinde especial.")
