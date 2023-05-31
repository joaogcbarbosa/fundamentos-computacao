temperaturas_celsius = [0.0] * 5
temperaturas_fahrenheit = [0.0] * 5
soma_fahrenheit = 0.0
soma_celsius = 0.0
acima_media_fahrenheit = 0

for i in range(5):
    temperaturas_celsius[i] = float(input("Temperatura em Celsius"))
    temperaturas_fahrenheit[i] = temperaturas_celsius[i] * 1.8 + 32
    soma_celsius += temperaturas_celsius[i]
    soma_fahrenheit += temperaturas_fahrenheit[i]

media_celsius = soma_celsius / 5
media_fahrenheit = soma_fahrenheit / 5

for i in range(5):
    if temperaturas_fahrenheit[i] > media_fahrenheit:
        acima_media_fahrenheit += 1

print("Temperatura média em Celsius: ", media_celsius)
print("Temperatura média em Fahrenheit: ", media_fahrenheit)
print("Total de temperaturas em Fahrenheit acima da média: ", acima_media_fahrenheit)
