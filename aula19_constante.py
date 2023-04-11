"""
    CONSTANTE - variável que nao vai mudar durante o programa
    não existe em python porém quando queremos que essa variável seja uma constante
    colocamos ea inteira em maiúsculo so para demonstra que não devemos muda-la
"""

VALOR_DOLAR = 5.6 #isso seria uma constante
saldo_real = 1000

saldo_convertido = saldo_real/VALOR_DOLAR

print(f"{saldo_convertido:.2f}")