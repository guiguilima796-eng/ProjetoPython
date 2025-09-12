import random
def somar(n1,n2):
    print(f"{n1} + {n2} = {n1 + n2}")

# somar(2,3)


def barra(n = 40 , char = "*"):
    print(n * char)

#barra()

def retangulo(largura,altura):
    for largura in range(altura):
        print("-")

def numeroAleatorio():
    for i in range(10):
        print(random.randint(1,1000000))

# numeroAleatorio()

# lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
# sorteio = random.choice(lista)
# print(sorteio)

lista = list(range(1,20))
listaEmbaralhada = lista[:]
print(listaEmbaralhada)
random.shuffle(listaEmbaralhada)
print(listaEmbaralhada)
print(random.sample(listaEmbaralhada,2))
