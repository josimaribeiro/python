Algoritmo "Programa6"

Var

   codigoTurma : inteiro
   qtdMasc, qtdFem : inteiro
   qtdApr,qtdRep,totalAlunos : inteiro
   porcMasc,porcFem,porcRep : real
Inicio
   escreva("Digite codigo turma :")
   leia(codigoTurma)

   escreva("Digite qtd Homens : ")
   leia(qtdMasc)

   escreva("Digite qtd Feminino : ")
   leia(qtdFem)

   escreva("Digite a qtd aprovador : ")
   leia(qtdApr)

   totalAlunos <- qtdMasc + qtdFem
   qtdRep <-  totalAlunos -  qtdApr
   porcMasc <- qtdMasc / totalAlunos * 100
   porcFem <-  qtdFem / totalAlunos * 100
   porcRep <- qtdRep / totalAlunos * 100
   escreval("Porcent Masc.........: ", porcMasc , " %")
   escreval("Porcent Fem..........: ", porcFem, " %")
   escreval("Porcent Reprovados...: ",porcRep, " %")
   escreval("Total de aluno.......: ",totalAlunos, " %")





Fimalgoritmo