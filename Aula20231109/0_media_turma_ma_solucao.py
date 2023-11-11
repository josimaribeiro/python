"""
Faça um programa que leia a nota final de 10 alunos de uma turma,
mostre a média e quantas notas estão acima da média:

o programa abaixo não é a mlehor solução, maisa frente
veremos uma melhor solução usando array

"""
n1 = float(input("Digite a nota 1 "))
n2 = float(input("Digite a nota 2 "))
n3 = float(input("Digite a nota 3 "))
n4 = float(input("Digite a nota 4 "))
n5 = float(input("Digite a nota 5 "))
n6 = float(input("Digite a nota 6 "))
n7 = float(input("Digite a nota 7 "))
n8 = float(input("Digite a nota 8 "))
n9 = float(input("Digite a nota 9 "))
n10 = float(input("Digite a nota 10 "))
media = (n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10) / 10
qtd_maior_media = 0
print("Media : ", media)
if n1 > media:
    qtd_maior_media += 1
if n2 > media:
    qtd_maior_media += 1
if n3 > media:
    qtd_maior_media += 1
if n4 > media:
    qtd_maior_media += 1
if n5 > media:
    qtd_maior_media += 1
if n6 > media:
    qtd_maior_media += 1
if n7 > media:
    qtd_maior_media += 1
if n8 > media:
    qtd_maior_media += 1
if n9 > media:
    qtd_maior_media += 1
if n10 > media:
    qtd_maior_media += 1

print("A qtd de notas superiores a media é ", qtd_maior_media)