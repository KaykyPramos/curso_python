nome = input('digite o seu nome:')
nome_tamanho = len(nome)
if nome_tamanho <= 4:
    print("seu nome é pequeno")
elif nome_tamanho >= 5 and nome_tamanho <= 6:
    print("seu nome é médio")
elif nome_tamanho > 6:
    print("seu nome é grande")
else:
    print("erro")