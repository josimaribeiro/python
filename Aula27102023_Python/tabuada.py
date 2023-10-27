numero = int(input("Qual tabuada voce quer saber? Digite um numero de 1 a 10.\n"))

while (numero < 0) or (numero > 10):
    numero = int(input("Qual tabuada voce quer saber? Digite um numero de 1 a 10.\n"))



print(" Tabuada do ", numero, ":\n")
for i in range(1, 11):
    print(numero, " X ", i, " = ", numero * i, "\n")
