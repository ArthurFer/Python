frutas = ["Pêra", "Uva", "Maçã", "Goiaba"]

for fruta in frutas:
    print(fruta)

print("--------------------------\n\n")

#Impressão do índice com função enumerate
for index, fruta in enumerate(frutas):
    print(f"{index}: {fruta}")