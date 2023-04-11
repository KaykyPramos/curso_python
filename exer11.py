while True:
    print("-"*40)
    num1 = input('digite um número:')
    num2 = input('digite um número:')
    ope = input("digite uma operação:+ - * /:")
    try:
        num1 = float(num1)
        num2 = float(num2)
    except:
        print("números inválidos")
        continue
    if ope not in "+-*/" or len(ope) < 1:
        print("operadores inválidos")
        continue
    if ope == "+":
        total = num1 + num2
        print(f"{num1} + {num2} = {total}")
    elif ope == "-":
        total = num1 - num2
        print(f"{num1} - {num2} = {total}")
    elif ope == "*":
        total = num1 * num2
        print(f"{num1} * {num2} = {total}")
    elif ope == "/":
        total = num1 / num2
        print(f"{num1} / {num2} = {total:.2f}")
    sair = input("[s]air?:").lower().startswith("s")
    if sair:
        print("falou")
        break