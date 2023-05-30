from random import randint

vetor = [0] * 30

x = int(input("x: "))

cont_x = 0
for i in range(0, 30):
    vetor[i] = randint(0, 15)
    if vetor[i] == x:
        cont_x += 1

print(vetor)
print(cont_x)
