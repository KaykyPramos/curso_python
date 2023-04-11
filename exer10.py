nome = "kayky"
indi = 0
novo_nome = "*"
while indi < len(nome):
    novo_nome += f"{nome[indi]}*"
    indi += 1
print(novo_nome)