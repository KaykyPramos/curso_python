'''
    o (if , elif) serve pra executar um bloco de código caso uma uma condição seja verdadeira 
    o else ocorre  caso todas as condições sejam falsa
''' 
condicao = input("Quer entrar ou sair? ")
if condicao == "entrar":
    print("entrou")
elif condicao  == "sair":
    print("saiu")
else:
    print("foi mal")