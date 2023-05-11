s = input("Digite algo: ")
nova_s = ""
vogais = "aeiou"

for i in range(len(s)):
    duplicou = False
    for j in range(len(vogais)):
        if s[i] == vogais[j]:
            nova_s += 2 * s[i]
            duplicou = True
    if not duplicou:
        nova_s += s[i]

print(nova_s)
