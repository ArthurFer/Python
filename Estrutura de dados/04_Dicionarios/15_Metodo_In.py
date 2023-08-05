contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "6523-5121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3365-2671"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-2299"},

}

resultado = "guilherme@gmail.com" in contatos # Metodo para verificar se a chave está no dicionario
print(resultado)

resultado = "meu@gmail.com" in contatos
print(resultado)

resultado = "idade" in contatos["chappie@gmail.com"] # Verifica se existe no dicionario interno
print(resultado)

resultado = "telefone" in contatos ["giovanna@gmail.com"]
print(resultado)
