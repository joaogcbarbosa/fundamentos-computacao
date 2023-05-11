s = input("Digite uma palavra para inverter sílaba a sílaba: ")
s_invertida = ""

for i in range(len(s)):
    if i % 2 != 0:
        s_invertida += s[i] + s[i - 1]

print("A palavra invertida é:", s_invertida.upper())
