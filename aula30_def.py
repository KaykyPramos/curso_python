# por padrão toda função retorna None

def soma(x,y): #definição
    return x+y
def subtrair(x,y,z = None):
    if z is not None:
        print(f"{x=} {y=} {z=} | {x-y-z}")
    else:
        print(f"{x=} {y=} | {x-y}")
       

soma1 = soma(y=2,x=7) #caso utilizamos parâmetros nomeados o parâmetro após o nomeado deve ser nomeado tbm
subtrair(10,7)
subtrair(10,z=0,y=4)

print(soma1)