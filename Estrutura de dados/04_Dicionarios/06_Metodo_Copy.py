contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "6523-5121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3365-2671"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-2299"},

}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

print(contatos["giovanna@gmail.com"])
print(copia["guilherme@gmail.com"])
