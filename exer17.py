def mult(*numeros):
    total = 1
    for num in numeros:
        total *= num
    return total

print("digite os números ou [S]air:")
numeros = []
while True:
    numero = input("R:").lower()
    if numero == "s":
        break
    try:
        numero_int = int(numero)
    except ValueError:
        print("digite algo valido")
        continue
    numeros.append(numero_int)
total = mult(*numeros)
print(total)

    