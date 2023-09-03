from builtins import input, print

nome = input("Digite o nome ")
nota1 = float(input("Digite a nota 1 : "))
nota2 = float(input("Digite a nota 2 : "))
media = (nota1 + nota2) / 2
print("Média ",media)
if media < 7:
    print("Reprovado")
else:
    print("Aprovado")
