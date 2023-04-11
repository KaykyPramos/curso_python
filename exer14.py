import os
lista = []
while True:
    sit = input("[A]dd [D]elet [L]ist:").lower()

    if sit not in "adl" or len(sit) > 1:
        os.system("cls")
        print("digite algo valido")
        continue
    elif sit == "a":
        valor = input("Digite o valor a ser add:")
        lista.append(valor)
        os.system("cls")
        print("Valor adicionado")
        continue
    elif sit == "d":
        if lista == []:
            os.system('cls')
            print("lista vazia")
            continue
        else:
            indice = input("Digite o índice a ser apagado:")
            try:
                indice = int(indice)
            except:
                os.system("cls")
                print("digite algo valido")
                continue
            if indice < len(lista):
                lista.pop(indice)
                os.system("cls")
                print("Valor apagado")
                continue                
            else:
                os.system("cls")
                print("digite algo valido")
                continue
    elif sit == "l":
        if lista == []:
            os.system('cls')
            print("lista vazia")
            continue
        else:
            os.system("cls")
            for ind,val in enumerate(lista):
                print(f"índice:{ind} valor:{val}")