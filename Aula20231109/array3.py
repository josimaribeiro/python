"""
Programa que solicita o nome e a altura de X atletas , depois mostre apenas 
os atletas com mais de 1.70m
"""

TAM = 4
nome = []
altura = []

for i in range(TAM):
    nome.append(input("Digite o nome : "))
    altura.append(float(input("Digite a altura  : ")))

for i in range(TAM):
    if altura[i]> 1.70:
        print("Nome : ",nome[i], " Altura ", altura[i])
    # fim se
# fim para