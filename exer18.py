def par_impar(num):
    sit = num%2 == 0
    if sit:
        return f"o número {numero} é Par"
    return f"o número {numero} é Ímpar"


numero = int(input("digite um número:"))
sit = par_impar(numero)

print(sit)