cadeia = input("Digite algo para checar se é palíndromo: ")

cadeia_inversa = ""

for i in range(len(cadeia) - 1, -1, -1):
    cadeia_inversa += cadeia[i]

if cadeia_inversa == cadeia:
    print("é palíndromo")
else:
    print("não é palíndromo")
