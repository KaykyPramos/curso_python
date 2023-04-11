nome = input('Qual seu nome?:')
idade = input('Qual sua idade?:')
if bool(nome) and bool(idade):
    print(f"sau nome é {nome}") 
    print(f"sau nome invertido é {nome[::-1]}")
    if ' ' in nome:
        print(f"seu nome contém espaços")
    else:
        print("seu nome NÃO contém espaços")
    print(f"seu nome tem {len(nome)} letras")
    print(f"a primeira letra do sue nome é {nome[0]}")
    print(f"a última letra do sue nome é {nome[-1]}")
else:
    print('Desculpa, voce deixou campos em vazios.')