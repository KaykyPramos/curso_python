'''
    try - tenta executar um código
    except - ocorreu um erro ao executar o código
'''

numero_str = input("vou dobrar o numero:")

try:
    numero_float = float(numero_str)
    print(f'o dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print("isso não é um número!")