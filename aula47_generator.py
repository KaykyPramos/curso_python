# generator é um iterador porem tbm é uma funçao que pode pausar/ um iterador nao é um generator
# é mais leve que uma lista pois é uma função e uma lista guarda todos os valores na memoria 

lista = [n for n in range(40)]
gerador = (i for i in range (40))

# print(lista)
# print(next(gerador))

def generator (n=0, maximum=10):
    while True:
        yield n
        n+=1
gen = generator()

for n in gen:
    print(n)
