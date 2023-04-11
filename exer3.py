primeiro_valor = input("digite um número: ")
segundo_valor = input("digite um número: ")

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior que {segundo_valor=}' )
elif segundo_valor > primeiro_valor:
    print(f'{segundo_valor=} é maior que {primeiro_valor=}' )
else:
    print(f'{primeiro_valor=} é igual {segundo_valor=}' )
