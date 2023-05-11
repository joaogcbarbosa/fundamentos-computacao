s = input("Digite algo: ")
char = input("Digite um caractere: ")

count_char = 0
for i in range(len(s)):
    if s[i] == char:
        count_char += 1

print('O caractere "', char, '" aparece', count_char, "vez(es) na string inserida.")
