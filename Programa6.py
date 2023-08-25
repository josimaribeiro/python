codigoTurma =  input("Digite codigo turma :")
qtdMasc = int(input("Digite qtd Homens : "))
qtdFem = int(input("Digite qtd Feminino : "))
qtdApr =int(input("Digite a qtd aprovados : "))
totalAlunos = qtdMasc + qtdFem
qtdRep = totalAlunos - qtdApr
porcMasc = qtdMasc / totalAlunos * 100
porcFem = qtdFem / totalAlunos * 100
porcRep = qtdRep / totalAlunos * 100
print("-----------------------------------------------")
print("Porcent Masc.........: ", porcMasc , " %")
print("Porcent Fem..........: ", porcFem, " %")
print("Porcent Reprovados...: ", porcRep, " %")
print("Total de aluno.......: ", totalAlunos)
print("-----------------------------------------------")
