from random import randint

mat = []

for i in range(0, 3):
    mat.append(0)
    mat[i] = []
    for j in range(0, 3):
        mat[i].append(randint(0, 50))

soma_principal = 0
soma_secundaria = 0

for i in range(0, 3):
    for j in range(0, 3):
        if i == j:
            soma_principal += mat[i][j]
        if i + j == 2:
            soma_secundaria += mat[i][j]

print(mat)
print("Soma dos elementos da diagonal principal:", soma_principal)
print("Soma dos elementos da diagonal secundária:", soma_secundaria)
