nomes = ["kayky","sandra","sabrina"]

lista_enumerada = list(enumerate(nomes))

print(lista_enumerada)

for item in enumerate(nomes): # funciona com qualquer iterável str,lista,tupla
    print(item)

for ind,val in enumerate(nomes): #podemos fazer o desempacotamento direto no for o python vai entender como colocar os valores nas variáveis
    print(ind,val)