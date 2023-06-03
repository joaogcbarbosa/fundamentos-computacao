from random import randint

mat = []

for i in range(0, 5):
    mat.append(0)
    mat[i] = []
    for j in range(0, 5):
        mat[i].append(randint(0, 50))

maior = 0
linha = 0
coluna = 0
for i in range(0, 5):
    for j in range(0, 5):
        if i == 0 and j == 0:
            maior = mat[i][j]
            linha = i
            coluna = j
        elif mat[i][j] > maior:
            maior = mat[i][j]
            linha = i
            coluna = j

print(mat)
print("Maior elemento da matriz:", maior)
print("Linha:", linha)
print("Coluna:", coluna)
