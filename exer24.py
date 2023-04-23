def zipper(capitais,siglas):
    intervalo = min(len(capitais),len(siglas))
    return [(capitais[i],siglas[i]) for i in range(intervalo)]

capitais = ['Salvador','São Paulo','Rio de Janeiro','Belo Horizonte']
siglas = ['BA','SP','RJ','MG']

print(*zipper(capitais,siglas), sep='\n')