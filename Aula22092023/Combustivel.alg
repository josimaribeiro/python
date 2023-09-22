Algoritmo "Combustivel"

Var
   combustivel : inteiro
   litro,total : real
   precoA : real
   precoG : real

Inicio
   precoA <- 2.90
   precoG <- 3.30

   repita
      escreval("Tipo de combustivel")
      escreval("1 - Álcool")
      escreval("2 - Gasolina")
      leia(combustivel)
   ate ((combustivel = 1) ou (combustivel = 2))

   escreval ("Quantos litros: ")
   leia (litro)

   //para Álcool
   se (litro<=20) e (combustivel=1) entao
      total := precoA*(litro*(1-(3/100)))
      escreval ("Valor total à pagar: R$ " ,total)
   senao
      se (litro>20) e (combustivel=1) entao
         total := precoA*(litro*(1-(5/100)))
         escreval ("Valor total à pagar: R$ " ,total)
      senao
         //para Gasolina
         se (litro<=20) e (combustivel=2) entao
            total := precoG*(litro*(1-(4/100)))
            escreval ("Valor total à pagar: R$ " ,total)
         senao
            se (litro>20) e (combustivel=2) entao
               total := precoG*(litro*(1-(6/100)))
               escreval ("Valor total à pagar: R$ " ,total)
            fimSe
         fimSe
      fimSe
   fimSe


Fimalgoritmo