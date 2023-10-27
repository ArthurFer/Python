

# class palavras:
#     def __init__(self, cifra_secreta):
#         self.cifra_secreta = cifra_secreta
#
#     def

import random


def jogar():
    print("************************************")
    print("***********Jogo da Forca************")
    print("************************************")

    arquivo = open("palavras.txt", "r")
    palavra = []

    for linha in arquivo:
        linha = linha.strip()
        palavra.append(linha)

    numero = random.randrange(0, len(palavra))
    palavra_secreta = palavra[numero]
    print(palavra_secreta)
    letras_acertadas = ["_" for letra in palavra_secreta]


    acertou = False
    enforcou = False
    erros = 0

    print(letras_acertadas)

    while not acertou and not enforcou:
        chute = input("Qual letra? ")
        if chute in palavra_secreta:
            posicao = 0
            for letra in palavra_secreta:
                if chute.upper() == letra.upper():
                    print(f"Encontrei a letra {letra} na posição {posicao} ")
                    letras_acertadas[posicao] = letra
                posicao += 1
        else:
            erros += 1
        acertou = "_" not in letras_acertadas
        enforcou = erros == 6
        print(letras_acertadas)

    if acertou:
        print("Você ganhou!")
    else:
        print("Você perdeu!")
    print("Fim de jogo")

jogar()