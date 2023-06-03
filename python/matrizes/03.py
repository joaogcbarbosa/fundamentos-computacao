mat = []

for i in range(0, 5):
    mat.append(0)
    mat[i] = []
    for j in range(0, 5):
        if i == j:
            mat[i].append(1)
        else:
            mat[i].append(0)

for i in range(0, 5):
    for j in range(0, 5):
        print(mat[i][j], end="  ")
    print()
