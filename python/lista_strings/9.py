s = input("Digite algo para verificar se é palíndromo: ")
s_invertida = ""

for i in range(len(s) - 1, -1, -1):
    s_invertida += s[i]

if s == s_invertida:
    print('É palíndromo')
else:
    print('Não é palíndromo')
