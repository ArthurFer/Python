contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "6523-5121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3365-2671"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-2299"},

}

contatos.update({"guilherme@gmail.com": {"nome": "Gui"}}) # Atualiza a chave com apenas "nome"
print(contatos)

contatos.update({"giovanna@gmail.com": {"nome": "Gio", "telefone": "3215-2573"}}) # Atualiza o dicionario original para os parametros passados
print(contatos)
