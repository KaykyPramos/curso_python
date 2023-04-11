texto = "Python"
numeros = range(7,17,2) # o range é composto pelo (inicio,fim,passos,)
# caso o fim seja negativo o inicio tem que ser menor
# caso so um valor for informado vai ser o valor final e começar no 0 
for numero in numeros:
    print(numero) 
for letra in texto:
    print(letra)

# iterável - str range entre outros sao iterativo
# iterador - quem sabe entregar um valor por vez
# next - me entrega o proximo valor
# iter = me mostra o iterador

# o for funciona da seguinte maneira criando um for com o while
texto = "kayky"
iterador = iter(texto)
while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break