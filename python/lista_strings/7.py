s = input("Digite uma palavra para invertê-la: ")
s_invertida = ""

for i in range(len(s) - 1, -1, -1):
    s_invertida += s[i]

print("A palavra invertida é:", s_invertida.upper())
