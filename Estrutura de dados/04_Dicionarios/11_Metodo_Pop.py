contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

resultado = contatos.pop("guilherme@gmail.com") # Remove a chave selecionada
print(resultado) # Mostra qual a chave removida

resultado = contatos.pop("guilherme@gmail.com", "não encontrado") # Retorna o segundo argumento se a chave já foi removida
print(resultado) # Mostra a mensagem


novos_contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "6523-5121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3365-2671"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-2299"},

}

print("----------------------------------------------")
for chave, valor in novos_contatos.items():
    print(chave,valor,"\n")

novos_contatos.popitem() # Remove as chaves do dicionário

print("---------------------------------------------")

for chave, valor in novos_contatos.items():
    print(chave,valor,"\n")


print("---------------------------------------------")
novos_contatos.popitem()


for chave, valor in novos_contatos.items():
    print(chave,valor,"\n")

