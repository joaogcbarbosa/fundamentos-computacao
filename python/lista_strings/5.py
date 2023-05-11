s = input("Digite algo: ")
nova_s = ""

for i in range(len(s)):
    nova_s += 2 * s[i]

print("String com letras duplicadas:", nova_s)
