n = int(input("Quantidade de alunos na turma: "))

notas = [0.0] * n
soma_notas = 0
cont_maior = 0

for i in range(0, n):
    notas[i] = float(input("Nota: "))
    soma_notas += notas[i]

media_turma = soma_notas / n

for i in range(0, n):
    if notas[i] >= media_turma:
        cont_maior += 1

print(cont_maior, "alunos acima da média")
print(n - cont_maior, "alunos abaixo da média")
