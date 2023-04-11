'''
    lista é um tipo do python diferente dos tipos anteriores essa é mutável
    suporta varios valores de varios tipos
    métodos uteis append insert pop del clear extend
'''
#índices  0      1       2    3    4 
lista = [123, "Kayky", True, [], 1.2]
#índices -1     -2      -3   -4   -5 
print(lista)
lista[1] = "sandra" 
print(lista)
print(lista[1])
print(lista[1][2])
#del lista[] deleta um item da lista com o índice informado pode causar problemas de processamento caso a lista seja grande
#lista.append adiciona ume item ao final da lista
#lista.pop() apaga o ultimo valor da lista retorna o valor apagado
#lista.clear() apaga todos os itens da lista
#lista.inset(índice,valor) adiciona um item e uma posição definida pode causar problemas de processamento caso a lista seja grande
# o + concatena listas
# lista_a.extend(lista_b) - junta o valor da lista b no final da lista a