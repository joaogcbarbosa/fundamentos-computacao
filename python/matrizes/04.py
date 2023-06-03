from random import randint

mat = []

for i in range(0, 6):
    mat.append(0)
    mat[i] = []
    for j in range(0, 6):
        mat[i].append(randint(0, 50))

c = 0
for i in range(0, 6):
    for j in range(0, 6):
        if mat[i][j] > 10:
            c += 1

print(mat)
print(c, "elementos maiores que 10 na matriz.")
