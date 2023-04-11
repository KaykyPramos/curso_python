# funciona como uma lista porem nao pode ser alterada ou seja é imutável

nomes = "kayky","sandra","sabrina" # pode ser so os valores ou os valores entre ()
# posso converter uma lista em tupla com tuple(lista)
# ou posso converter uma tupla em lista com o list(tupla)

nome, *_ = nomes
print(nome)

lista_enumerada = list(enumerate(nomes))

for item in enumerate(nomes): # funciona com qualquer iterável str,lista,tupla
    print(item)
print(lista_enumerada)