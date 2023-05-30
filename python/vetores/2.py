vetor = [0] * 12

for i in range(0, 12):
    vetor[i] = int(input("Valor: "))

x = int(input("X: ")) - 1
y = int(input("Y: ")) - 1

soma = 0
for i in range(0, 12):
    if i == x or i == y:
        soma += vetor[i]

print(soma)
