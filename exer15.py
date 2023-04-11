import re
import sys

entrada = input("digite seu cpf:")
cpf = re.sub(r'[^0-9]','', entrada)#.replace(".","").replace("-","")

if cpf == cpf[0]*len(cpf):
    print("nao aceitamos cpf repetido")
    sys.exit()

nove_digitos = cpf[:9]
val_regressivo1 = 10
result_digit_1 = 0

for digito in nove_digitos:
    result_digit_1 += int(digito)*val_regressivo1
    val_regressivo1-=1
digito_1 = (result_digit_1*10)%11
digito_1 = 0 if digito_1>9 else digito_1

dez_digitos = cpf[:10]
val_regressivo = 11
result_digit_2 = 0

for novo_digito in dez_digitos:
    result_digit_2 += int(novo_digito)*val_regressivo
    val_regressivo-=1
digito_2 = (result_digit_2*10)%11
digito_2 = 0 if digito_2>9 else digito_2


digitos = str(digito_1)+str(digito_2)
confirmador = cpf[9:]
print("cpf verdadeiro" if confirmador==digitos else "cpf falso")