hora = input("digite a hora do dia (sistema 24h)\nR:")
manha = None
tarde = None
noite = None
try:
    hora = int(hora)
    manha = hora >= 0 and hora <= 11
    tarde = hora >= 12 and hora <= 17
    noite = hora >= 18 and hora <= 23
    if manha:
        print("bom dia")
    elif tarde:
        print("boa tarde")
    elif noite:
        print("boa noite")
    else:
        print("erro")
except:
    print("o valor digitado não esta no formato 24h")