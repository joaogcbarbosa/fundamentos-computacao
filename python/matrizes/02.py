from random import randint

mat = []

for i in range(0, 7):
    mat.append(0)
    mat[i] = []
    for j in range(0, 7):
        mat[i].append(randint(0, 50))

soma_linha_6 = 0
soma_coluna_2 = 0
soma_diagonal = 0
elemento_3_4 = 0
soma_pares = 0
for i in range(0, 7):
    for j in range(0, 7):
        if i == 5:
            soma_linha_6 += mat[5][j]
        if j == 1:
            soma_coluna_2 += mat[i][1]
        if i == j:
            soma_diagonal += mat[i][j]
        if i == 2 and j == 3:
            elemento_3_4 = mat[2][3]
        if mat[i][j] % 2 == 0:
            soma_pares += mat[i][j]

print(mat)
print("Soma dos elementos da linha 6:", soma_linha_6)
print("Soma dos elementos da coluna 2:", soma_coluna_2)
print("Soma dos elementos da diagonal principal:", soma_diagonal)
print("Elemento na posição 3x4:", elemento_3_4)
print("Soma dos elementos pares da matriz:", soma_pares)
