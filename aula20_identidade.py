"""
    Flags - marca um local
    None - não valor
    is e is not  - é ou não é (tipo, valor, identidade)
    id - identidade
        caso o valor de 2 ou mais variáveis sejam iguais o python vai usar o memos id
        o python vai salvar o uma das variáveis e vai atribuir os apelidos ao mesmo local na memória
"""

condicao = True
pass_if = None

if condicao:
    pass_if = True
    print(id(condicao))
else:
    print("outro codigo")

if pass_if is None:
    print("passou dentro do if")
elif pass_if is not None:
    print("nao passou no if")