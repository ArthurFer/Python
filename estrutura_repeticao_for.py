texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
print()

#for numero in range(0, 61, 2):
#    print(numero, end=" ")

for numero in range(100):
    if numero % 2 == 0:
        continue

    print(numero, end=" ")

print("\n")

for numero in range(100):
    if numero % 2 != 0:
        continue

    print(numero, end=" ")