vetor = [0] * 10

c = 0
for i in range(0, 20):
    if i % 2 == 1:
        vetor[c] = i
        c += 1

print(vetor)
