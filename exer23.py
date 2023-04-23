def soma(x,y):
    return x+y

def multplica(x,y):
    return x*y

def cria_funcao(func,x):
    def interna(y):
        return func(x,y)
    return interna

soma_com_cinco = cria_funcao(soma,5)
multplica_por_dez = cria_funcao(multplica,10)

print(soma_com_cinco(20))
print(multplica_por_dez(5))