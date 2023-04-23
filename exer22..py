import copy
produtos = [
    {'nome': 'Produto 5','preco':10.00},
    {'nome': 'Produto 1','preco':22.32},
    {'nome': 'Produto 3','preco':10.11},
    {'nome': 'Produto 2','preco':105.87},
    {'nome': 'Produto 4','preco':69.90},
]

novos_produtos = copy.deepcopy(produtos)

novos_produtos = [{**produto, 'preco' : round(produto['preco'] * 1.1,2)}
    for produto in produtos
    ]

novos_produtos_ordenado_nome = sorted(novos_produtos,key=lambda p: p["nome"],reverse=True)

novos_produtos_ordenado_preco = sorted(novos_produtos,key=lambda p: p["preco"])
print(*produtos, sep="\n")
print()
print(*novos_produtos, sep="\n")
print()
print(*novos_produtos_ordenado_nome, sep="\n")
print()
print(*novos_produtos_ordenado_preco, sep="\n")
