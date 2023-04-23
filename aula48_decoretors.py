def decorador(func):
    def interna (*args):
        for n in args:
            e_num(n)
        return func(*args)
    return interna

@decorador
def soma(x,y):
    return x+y

def e_num(arg):
    if not isinstance(arg,int):
        raise ValueError
    

somar = soma(6,6)

print(somar)
