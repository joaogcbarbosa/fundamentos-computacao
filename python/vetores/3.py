from random import randint

vetor_inicial = [0] * 16
vetor_final = [0] * 16

for i in range(0, 16):
    vetor_inicial[i] = randint(-100, 100)

for i in range(0, 16):
    if i < 8:
        vetor_final[i] = vetor_inicial[i + 8]
    else:
        vetor_final[i] = vetor_inicial[i - 8]

print(vetor_inicial)
print(vetor_final)
