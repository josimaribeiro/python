Algoritmo "estrutura_repeticao"
// Este programa usa “PARA” e repete todo código dentro do loop n vezes
// Usamos o “PARA” quando sabemos quantas vezes o loop precisa repetir

Var
   matricula,cont : inteiro
   salario_bruto,desconto,salario_liquido : real
Inicio

   para cont de 1 ate 2 faca
      escreva("Digite a matricula do funcionario :")
      leia(matricula)
      escreva("Digite o salario :")
      leia(salario_bruto)
      desconto <- salario_bruto * 8 / 100
      salario_liquido <- salario_bruto - desconto
      escreva("O salario liquido é :",salario_liquido)
      escreva("O desconto foi : ",desconto)
      escreval("")
   fimpara
Fimalgoritmo
