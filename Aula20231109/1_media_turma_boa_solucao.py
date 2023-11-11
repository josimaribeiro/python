"""
Faça um programa que leia a nota final de 10 alunos de uma turma,
mostre a média e quantas notas estão acima da média:
"""
TAM = 10
nota = []
acumulado = 0.0
maior_que_media = 0

for i in range(TAM):
    nota.append(float(input("Digite a nota  : ")))
    acumulado += nota[i]

media = acumulado / TAM
print("Media ..........................: {:.2f}".format(media))
for i in range(TAM):
    if nota[i] > media:
        maior_que_media += 1
    # fim se
# fim para
print("Total de notas acima da média...: ", maior_que_media)