from random import randint

mat = []
mat_trocada = []

for i in range(0, 4):
    mat.append(0)
    mat_trocada.append(0)
    mat[i] = []
    mat_trocada[i] = []
    for j in range(0, 4):
        mat[i].append(randint(0, 50))
        mat_trocada[i].append(0)

c = 0
for i in range(0, 4):
    for j in range(0, 4):
        if i == 1:
            mat_trocada[1][j] = mat[c][3]
            c += 1
        else:
            mat_trocada[i][j] = mat[i][j]

print(mat)
print(mat_trocada)
