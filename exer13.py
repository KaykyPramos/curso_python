import os

PALAVRA = 'lolipop'
acerto = ''
tentativas = 0 

while True:
    letra_digitada = input("Digite uma letra:")
    if len(letra_digitada) > 1:
        print("Digite apenas uma letra!")
        continue
    tentativas += 1

    if letra_digitada in PALAVRA:
        acerto += letra_digitada
    palavra_formada = '' 

    for letra_secreta in PALAVRA:
        if letra_secreta in acerto:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print("palavra secreta:",palavra_formada)
    if palavra_formada == PALAVRA:
        os.system("cls")
        print("VOCÊ GANHOU!!")
        print(f"você acertou em {tentativas}")
        acerto = ''
        tentativas = 0 
