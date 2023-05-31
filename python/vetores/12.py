# vetores de inteiros positivos

vet1 = [0] * 10
vet2 = [0] * 10
vet_total = [0] * 20
cont_repetidos = 0

# preenchendo vetor 1, vetor 2 e um vetor total contendo os elementos de ambos vetores
for i in range(20):
    if i < 10:
        vet1[i] = int(input("Valor para VETOR 1: "))
        vet_total[i] = vet1[i]
    else:
        vet2[i - 10] = int(input("Valor para VETOR 2: "))
        vet_total[i] = vet2[i - 10]

# trocando possíveis valores repetidos do vetor total por inteiros negativos e contando-os
c = 0
for i in range(20):
    for j in range(i + 1, 20):
        if vet_total[i] == vet_total[j]:
            vet_total[j] = -9999 + c
            c += 1
            cont_repetidos += 1

# inicializando o vetor que irá conter a união dos elementos do vetor 1 com vetor 2
vet_uniao = [0] * (len(vet1) + len(vet2) - cont_repetidos)

# preenchendo o vetor união com os inteiros válidos (positivos) e ignorando os possíveis inválidos (negativos)
j = 0
for i in range(20):
    if vet_total[i] > 0:
        vet_uniao[j] = vet_total[i]
        j += 1

# botando o vetor união em ordem
for i in range(len(vet_uniao)):
    for j in range(i + 1, len(vet_uniao)):
        if vet_uniao[j] < vet_uniao[i]:
            aux = vet_uniao[i]
            vet_uniao[i] = vet_uniao[j]
            vet_uniao[j] = aux

# trocando possíveis valores repetidos do vetor 1 por inteiros negativos e contando-os
c = 0
cont_invalidos_1 = 0
for i in range(10):
    for j in range(i + 1, 10):
        if vet1[i] == vet1[j]:
            vet1[j] = -9999 + c
            c += 1
            cont_invalidos_1 += 1

# trocando possíveis valores repetidos do vetor 2 por inteiros negativos e contando-os
c = 0
cont_invalidos_2 = 0
for i in range(10):
    for j in range(i + 1, 10):
        if vet2[i] == vet2[j]:
            vet2[j] = -9999 + c
            c += 1
            cont_invalidos_2 += 1

# contando quantos são os elementos iguais válidos entre o vetor 1 e o vetor 2
iguais = 0
for i in range(10):
    for j in range(10):
        if vet1[i] == vet2[j] and vet1[i] > 0:
            iguais += 1

# inicializando o vetor que irá conter a interseção dos elementos do vetor 1 com vetor 2
vet_intersecao = [0] * iguais

# preenchendo o vetor interseção
k = 0
for i in range(10):
    for j in range(10):
        if vet1[i] == vet2[j] and vet1[i] > 0:
            vet_intersecao[k] = vet1[i]
            k += 1

# botando o vetor interseção em ordem
for i in range(len(vet_intersecao)):
    for j in range(i + 1, len(vet_intersecao)):
        if vet_intersecao[j] < vet_intersecao[i]:
            aux = vet_intersecao[i]
            vet_intersecao[i] = vet_intersecao[j]
            vet_intersecao[j] = aux

print("Vetor 1:", vet1)
print("Vetor 2:", vet2)
print("União:", vet_uniao)
print("Interseção:", vet_intersecao)
