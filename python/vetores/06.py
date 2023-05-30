from random import randint

vetor = [0] * 40

cont_par = 0
for i in range(0, 40):
    vetor[i] = randint(0, 50)
    if vetor[i] % 2 == 0:
        cont_par += 1

print(vetor)
print(cont_par)
