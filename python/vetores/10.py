frase = input("Digite uma frase: ")

VOGAIS = "aeiou"
cont_vogais = 0
cont_espaco = 0
cont_total = 0

for i in range(len(frase)):
    for j in range(len(VOGAIS)):
        if frase[i] == VOGAIS[j]:
            cont_vogais += 1
            break

    if frase[i] == " ":
        cont_espaco += 1

    cont_total += 1

print("Total de vogais: ", cont_vogais)
print("Total de espaços em branco: ", cont_espaco)
print("Restante: ", cont_total - cont_vogais - cont_espaco)
