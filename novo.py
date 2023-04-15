import os
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },{
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },{
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },{
        'Pergunta': 'Quanto é 9-3?',
        'Opções': ['3', '9', '-6', '6'],
        'Resposta': '6',
    },]
acertos = 0
def perguntar(i,acertos):
    print('Pergunta:',perguntas[i]["Pergunta"])
    print("Escolha uma Opção:")
    for op in enumerate(perguntas[i]["Opções"]):
        print(*op, sep=") ")
    escolha = input("R:")
    try:
        escolha_int = int(escolha)
        condicao =  perguntas[i]["Opções"][escolha_int] == perguntas[i]["Resposta"] and escolha_int >= 0
    except:
        condicao = False
    if condicao:
        print("Acertou ✔")
        acertos = acertos + 1
        return acertos
    print("Errou ❌")
    acertos = acertos + 0
    return acertos
    
for i in range(len(perguntas)):
    acertos = perguntar(i,acertos)
    print(" ")
os.system("cls")
print(f"você acertou {acertos} de {len(perguntas)}")