'''
troca 2 variáveis pelo método tradicional
sabemos que o python pode fazer isto de outra forma
mais fácil ex: 
[v1, v2] = [v2, v1]

'''

v1 = int(input("Digite v1 : "))
v2 = int(input("Digite v2 : "))
print("V1 vale = %2d " % (v1))
print("V2 vale = %2d " % (v2))
tmp = v1
v1 = v2
v2 = tmp
print("Agora V1 vale = %2d " % (v1))
print("Agora V2 vale = %2d " % (v2))
