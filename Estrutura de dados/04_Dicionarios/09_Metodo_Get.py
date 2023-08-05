contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

#print(contatos["chave"]) #KeyError

print(contatos.get("chave")) # Retorna NONE
print(contatos.get("chave",{})) # Retorna {}
print(contatos.get("guilherme@gmail.com", {})) # Retorna a chave selecionada




