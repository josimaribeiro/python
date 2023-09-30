import random
"""
faça um programa que sorteie um numero entre 1 e 10 peça ao usuário para 
dar um 'chute', mostre se ele acertou, se  o numero sorteado era menor ou
maior
"""
sort = random.randint(1, 10)

num = int(input("Digite um valor entre 1 e 10 : "))

if num == sort:
    print("Você acertou")
elif sort < num:
    print("o numero sorteado é menor")
else:
    print("o numero sorteado é maior")

print("O numero sorteado foi ", sort)
#fim