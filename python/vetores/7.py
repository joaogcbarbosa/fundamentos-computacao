from random import randint

vetor1 = [0] * 10
vetor2 = [0] * 10
vetor = [0] * 20

for i in range(0, 20):
    if i < 10:
        vetor1[i] = randint(0, 20)
    else:
        vetor2[i - 10] = randint(0, 20)

print(vetor1)
print(vetor2)

for i in range(0, 20):
    if i < 10:
        vetor[i] = vetor1[i]
    else:
        vetor[i] = vetor2[i - 10]

print(vetor)
