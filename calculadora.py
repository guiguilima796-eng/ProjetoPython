print("------CALCULADORA------")
try:
    n1 = float(input("Digite um Número :"))
    n2 = float(input("Digite outro Número :"))
    op = input("Escolha a opração:(+,-,x,/) :")

    match op.lower():
        case "+":
            resultado = n1 + n2
            print("-----------------------")
            print(f"{n1} + {n2} = {resultado}")
            print("-----------------------")
        case "-":
            resultado = n1 - n2
            print("-----------------------")
            print(f"{n1} - {n2} = {resultado}")
            print("-----------------------")
        case "x":
            resultado = n1 * n2
            print("-----------------------")
            print(f"{n1} x {n2} = {resultado}")
            print("-----------------------")
        case "/":
            try:
                resultado = n1 / n2
                print("-----------------------")
                print(f"{n1} / {n2} = {resultado}")
                print("-----------------------")
            except ZeroDivisionError:
                print("-----------------------")
                print("Erro: Divizão por Zero é inválida.")
                print("-----------------------")
        case _: # O padrão curinga (underscore) funciona como o 'default'
            print("-----------------------")
            print("Operação Inválida.")
            print("-----------------------")
    
    
except ValueError:
    print("-----------------------")
    print("[ERRO!] digite números!")
    print("-----------------------")