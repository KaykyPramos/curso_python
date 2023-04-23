produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# filtrando com list comprention
novos_produtos = [
    p for p in produtos
    if p["preco"] > 22
    ]

# usando o metodo filter
novos_produtos_lamb = filter(
    lambda p:p['preco'] > 100,
    produtos
)

print(*novos_produtos, sep="\n")
print()
print(*novos_produtos_lamb, sep="\n")