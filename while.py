#n = int(input("Digite um número para percorer os números pares entre 0 e ele:"))
#x = 0
#while x <= n:
#     if (x % 2 == 0):
#         print(x)
#     x +=1

# n1 = int(input("digite um número:"))

# for n in range(n1):
#     if(n % 2 == 0):
#         print(n)

# i = [1,2,3,4,5,6,7,8,9,10]
# print("ForEach")
# for n in i:
#     if(n % 2 == 0):
#         print(n)
# numero = 0
# while numero <=10:
#     if(numero % 2 ==0):
#         numero +=1
#         continue

#     print(numero)
#     numero +=1
soma = 0
for i in range(25,200):
    if(i % 2 == 0):
        soma +=i 
print(f"soma de 25 a 200 dos números Pares= {soma}")
