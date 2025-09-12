soma = 0

while True:
    valor = int(input("Digite um Valor a ser Somado ou 0 para Sair:"))

    if(valor == 0):
        break

    soma +=valor
print(soma)