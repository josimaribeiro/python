import random

sort = random.randint(1, 10)


num = int(input("Digite um valor entre 1 e 10 : "))

tentativa = 1

while num != sort:
    tentativa = tentativa + 1
    print("Voce errou")
    if sort < num:
        print("O numero sorteado é menor")
    else:
        print("O numero sorteado é maior")
    num = int(input("Digite um valor entre 1 e 10 : "))
print("_"*100)
print("Você acertou na tentativa ", tentativa)
print("O numero sorteado foi ", sort)
print("_"*100)