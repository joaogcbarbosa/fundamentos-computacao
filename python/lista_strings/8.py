s1 = input("Digite uma palavra: ")
s2 = input("Digite outra: ")

if len(s2) > len(s1):
    aux = s1
    s1 = s2
    s2 = aux

diferenca_tamanho = len(s1) - len(s2)

for i in range(diferenca_tamanho):
    s2 += " "

intersecao = ""

for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            intersecao += s1[i]

ALFABETO = "abcdefghijklmnopqrstuvwxyz"
intersecao_sem_repeticao = ""
for i in range(len(ALFABETO)):
    for j in range(len(intersecao)):
        if ALFABETO[i] == intersecao[j]:
            intersecao_sem_repeticao += ALFABETO[i].upper() + " "
            break

if intersecao_sem_repeticao:
    print("As letras em comum entre ambas palavras são:", intersecao_sem_repeticao)
else:
    print("Não há letras em comum entre as palavras.")
