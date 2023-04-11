import time
nome = "01010101010101010"
cont = 1
while True:
    while cont <= len(nome):
        print(nome[:cont])
        cont += 1
        time.sleep(0.2)
    while cont > 1:
        cont -= 1
        print(nome[:cont])
        time.sleep(0.2)