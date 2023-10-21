Algoritmo "Socios"

// Este programa usa “ENQUANTO” e repete todo código dentro do loop até
// uma variável de checagem for Verdadeira (true)
// Usamos o “ENQUANTO” quando NÃO sabemos quantas
//  vezes o loop precisa repetir

const SOCIOS = 3
Var
   valor_venda : real
   acumulado,valor_socio : real
   qtd_vendas : inteiro
Inicio

   acumulado <- 0
   qtd_vendas <- 0

   escreva("Digite o valor da venda : ")
   leia(valor_venda)
   enquanto valor_venda <> 0 faca
      acumulado <- acumulado + valor_venda
      qtd_vendas <- qtd_vendas + 1
      valor_socio <- acumulado / SOCIOS
      escreval("Acumulado :",acumulado:4:2)
      escreval("Cada sócio recebendo ",valor_socio:4:2)
      escreva("Digite o valor da venda : ")
      leia(valor_venda)
   fimenquanto
   escreval("Acumulado ",acumulado:4:2)
   escreval("Total de vendas" ,qtd_vendas)
Fimalgoritmo

