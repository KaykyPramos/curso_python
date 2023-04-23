def somar(l1,l2):
    inter = min (len(l1),len(l2))
    nova = []
    for i in range(inter):
        nova.append(l1[i] + l2[i])
    return nova

l1 = [3,4,7]
l2 = [4,8,0]
soma = somar(l1,l2)
print(soma)