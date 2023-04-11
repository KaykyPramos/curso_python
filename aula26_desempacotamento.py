nomes = ["kayky","sandra","sabrina"] 
print(nomes)
nome1,nome2,nome3 = nomes # vai salvar item por item nos nas variáveis
print(nome1,nome2,nome3)
# caso tenha mais variáveis que valores ou mais valores que variáveis vai dar erro
# caso queira pegar so o primeiro preciso dizer ao python oque fazer com o resto
nome, *_ = nomes
print(nome,_)
#é uma convenção do python usar "_" para esse resto pois assim quem olhar esse código vai saber que nao vai usar
print("-"*30)
# posso desempacotar direto na funçao sem jogar pra variavel 
salas = [["maria", "carla"], ["julia"], ["kayky", "raimundo"]]
print(*salas, sep='\n') 