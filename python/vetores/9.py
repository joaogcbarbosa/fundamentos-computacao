frase = input("Digite uma frase: ")

parada = 0
palavra = ""

for i in range(len(frase)):
    if frase[i] == " ":
        for j in range(parada, i):
            palavra += frase[j]
        print(palavra)
        palavra = ""
        parada = i + 1
    elif i == len(frase) - 1:
        for j in range(parada, i + 1):
            palavra += frase[j]
        print(palavra)

print(parada)
