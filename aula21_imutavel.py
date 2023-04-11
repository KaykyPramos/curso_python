"""
    valores imutáveis : str, int, float, bool
    são imutáveis pois não pode mudar o valor da variável sem mudar ela inteira 
"""
string = "kayky pereira"
# string[4] = "novo" no caso isso não pode ocorrer 
outra = f"{string[:4]}novo{string[5:]}"
print(string.capitalize())
print(outra)