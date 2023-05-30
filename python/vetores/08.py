from random import randint

vetor1 = [0] * 15
vetor2 = [0] * 15
vetor_soma = [0] * 15
vetor_diferenca = [0] * 15

for i in range(0, 30):
    if i < 15:
        vetor1[i] = randint(-10, 10)
    else:
        vetor2[i - 15] = randint(-10, 10)

for i in range(0, 15):
    vetor_soma[i] = vetor1[i] + vetor2[i]
    vetor_diferenca[i] = vetor1[i] - vetor2[i]

print(vetor1)
print(vetor2)
print(vetor_soma)
print(vetor_diferenca)
