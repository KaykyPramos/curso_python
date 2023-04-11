'''
    s - string
    d e i - int
    f - float
    x e X - hexadecimal
    caso utilizemos %04D por exemplo o primeiro numero (0) vai ser com o que o python vai preencher
    o segundo(4) é a quantidade de casas e a letra(D) mostra a variável
'''

nome = "kayky"
preco = 1000.568987

print("%s, o preço é R$%.2f" % (nome,preco)) # caso so tenha uma variável não usa os parenteses 
print("O Hexadecimal do numero %04d é %04x" % (178,178)) # o %x mostra o equivalente em hexadecimal