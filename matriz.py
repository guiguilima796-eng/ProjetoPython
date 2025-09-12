carros = ["fiat","Uno"]

def adicionarCarro(nomeCarro):
    carros.append(nomeCarro) 
    print("------------------------------------")
    print(f"{nomeCarro} Adicionado com Sucesso!")
    

def removerCarro(nomeCarro):
    carros.remove(nomeCarro) 
    print("------------------------------------")
    print(f"{nomeCarro} Removido com Sucesso!")
    

def listarCarros():
    print("------------------------------------")
    print("Lista de carros:")
    for carro in carros:
        print(carro)
    print("------------------------------------")

continuar = True

while continuar:
    print("------------------------------------")
    print("---------Estoque de Carros----------")
    print("------------------------------------")
    print("1-Adicionar Carro")
    print("2-Remover Carro")
    print("3-Listar Carros")
    print("4-Sair...")
    print("------------------------------------")
    op = int(input("Escolha uma dessas Opções:"))
    match op:
        case 1: 
            print("------------------------------------")
            nomeCarroAserAdicionado = input("Digite o nome do carro a ser Adicionado:") 
            adicionarCarro(nomeCarroAserAdicionado)
        case 2:
            print("------------------------------------")
            nomeCarroAserRemovido = input("Digite o nome do carro a ser removido:")
            removerCarro(nomeCarroAserRemovido)
        case 3:
            listarCarros()
        case 4:
            continuar = False
            break
        case _:
            print("[Erro] Opção Inválida !")

print("------------------------------------")
print("Progama Interrompido!")