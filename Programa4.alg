algoritmo "Programa4"

var
   nome : caracter
   salarioBruto,valorDesconto,salarioLiquido :real
inicio
   escreva("Digite o nome : ")
   leia(nome)

   escreva("Digite o salario : ")
   leia(salarioBruto)

   valorDesconto <- salarioBruto * ( 8 / 100)
   salarioLiquido <- salarioBruto - valorDesconto
   
   escreval("O desconto foi ",valorDesconto )
   escreval("O salario liquido é ",salarioLiquido)

fimalgoritmo