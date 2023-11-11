Algoritmo "juros_simples"
Var
   juros : real
   capital,montante : real
   i_taxa : real
   temp : inteiro
Inicio

   escreva("Digite o capital : ")
   leia(capital)
   escreva("Digite a taxa de juros : ")
   leia(i_taxa)
   i_taxa <- i_taxa / 100
   escreva("Digite o tempo :")
   leia(temp)
   juros <- capital * i_taxa *  temp
   escreval("O juros foi de ", juros)
   montante <- capital +  juros
   escreval("Seu montante é ",montante:4:2 )
   
Fimalgoritmo