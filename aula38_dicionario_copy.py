# copy - retorna uma cópia rasa (shallow copy)
# quando o dado é mutável e utilizamos o = e mudamos um dos valores vamos mudar das 2 variáveis
# usamos o copy para fazer essa copia ai caso mudamos os da dos imutáveis nao altera nas duas
# porem caso tenha uma dado mutável e mudarmos ele ainda vai mudar nas duas variáveis
# para isso temos a biblioteca copy e o método copy.deepcopy que copia o dado mutável inteiro    
import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
d2 = d1.copy() 

d2['c1'] = 1000
d2['l1'][1] = 999999

print(d1)
print(d2)