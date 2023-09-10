algoritmo "Programa5"
Var
   mat1,mat2 : inteiro
   nome1,nome2 : caracter
   salb1,salb2 : real
   saliq1, saliq2 : real
   desc5, acres9 : real


Inicio
   escreva("Digite mat do func 1 : ")
   leia(mat1)
   escreva("Digite nome func 1 : ")
   leia(nome1)
   escreva("Digite o sal bruto do func 1 : ")
   leia(salb1)
   escreva("Digite mat do func 1 : ")
   leia(mat2)
   escreva("Digite nome func 2 : ")
   leia(nome2)
   escreva("Digite o sal bruto do func 2 : ")
   leia(salb2)
   
   desc5 <- salb1 * ( 5 / 100)
   acres9 <- salb2 * ( 9 / 100)
   saliq1 <- salb1 - desc5
   saliq2 <-  salb2 + acres9

   escreval("Valor desc func 1 R$ ",desc5)
   escreval("Valor acrec func 2 R$ ",acres9)
   escreval("Salario liq func 1 R$ ",saliq1)
   escreval("Salario liq func 2 R$",saliq2)

Fimalgoritmo