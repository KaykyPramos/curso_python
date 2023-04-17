produtos = {
    'nome' : 'Caneta Azul',
    'preco' : 2.5,
    'categoria' : 'escritório',
}

dc = {
    chave:valor.capitalize()
    if isinstance(valor,str) else valor
    for chave,valor in produtos.items()
}

print(dc)