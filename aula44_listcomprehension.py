lista = []
for numero in range(10):
    lista.append(numero)
print(lista)

# posso colocar logica e tudo feito em uma linha
lista2 = [numero for numero in range(10)]
print(lista2)

# mapeamento de dados gera uma nova lista e posso alterar valores, as listas devem ser do mesmo tamanho

produtos = [
    {'nome' : 'chocolate' , 'preco' : 30,},
    {'nome' : 'sucrilhos' , 'preco' : 10,},
    {'nome' : 'coca cola' , 'preco' : 20,}
    ]
# oque esta a esquerda do for é mapeamento(colocar um dado de outra lista em uma lista nova) 
# oque esta a direita do for é um filtro so acrescenta na lista nova se a condição for verdadeira
produtos_corre = [
    {**produto, 'preco' : produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] > 10
    ]

print(*produtos_corre, sep= '\n')
