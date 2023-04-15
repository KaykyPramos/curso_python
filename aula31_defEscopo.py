x = 1

def escopo():
    def outra_funcao():
        y = 7 # essa variável foi definida dentro da função a função de fora e o parte principal nao tem acesso 
        print(f"{y=}")
    outra_funcao()
    print(f"{x=}")

escopo()