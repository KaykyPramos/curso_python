import os
perguntas = [
    {
        'Pergunta': 'Quanto é 43+5?',
        'Opções': ['50', '43', '48', '46'],
        'Resposta': '48',
    },{
        'Pergunta': 'Quanto é 25*4?',
        'Opções': ['125', '100', '115', '150'],
        'Resposta': '100',
    },{
        'Pergunta': 'Quanto é 100/2?',
        'Opções': ['40', '50', '20', '10'],
        'Resposta': '50',
    },{
        'Pergunta': 'Quanto é 16-9?',
        'Opções': ['7', '9', '8', '6'],
        'Resposta': '7',
    },{
        'Pergunta': 'Quanto é 10*5?',
        'Opções': ['20', '50', '40', '30'],
        'Resposta': '50',
    }]
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