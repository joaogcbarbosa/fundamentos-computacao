from random import randint

mat = []

for i in range(0, 4):
    mat.append(0)
    mat[i] = []
    for j in range(0, 4):
        mat[i].append(randint(0, 50))

elemento = int(input("Elemento que deseja encontrar na matriz: "))

linha = 0
coluna = 0
achou = False
for i in range(0, 4):
    for j in range(0, 4):
        if mat[i][j] == elemento:
            linha = i
            coluna = j
            achou = True
            break
    if achou:
        break

print(mat)
if achou:
    print("Elemento encontrado na linha", linha, "coluna", coluna)
else:
    print("Elemento não encontrado")
