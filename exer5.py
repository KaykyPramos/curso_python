num = input("digite um número:")
try:
    num_int = int(num)
    par_impar = num_int%2
    if par_impar == 0:
        print(f"o número {num} é par ")
    else:
        print(f"o número {num} é impar ")
except:
    print("o valor digitado não é um número inteiro ")