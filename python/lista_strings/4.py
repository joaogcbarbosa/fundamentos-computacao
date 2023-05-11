s = input("Digite algo: ")
char = input("Digite um caractere para remover da string inserida: ")
nova_s = ""

for i in range(len(s)):
    if s[i] != char:
        nova_s += s[i]

print("A nova string é:", nova_s)
