'''
    operadores lógicos
    and(e) - todas as condições precisam ser verdadeiras
    or(ou) - pelo menos uma condição precisa ser verdadeira
    not - inverter expressão
'''

entrada = input("[E]ntrar ou [S]air:")
senha= input("digite a senha:")

if (entrada == "E" or entrada == "e") and senha == "123":
    print("entrada com sucesso")
else:
    print('sair')