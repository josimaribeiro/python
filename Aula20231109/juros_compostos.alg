Algoritmo CalculoJurosCompostos
Var
   valorInicial, taxaJuros, tempo, montante: Real
   contador: Inteiro

Inicio
   // Solicita os valores ao usuário
   Escreva("Digite o valor inicial: ")
   Leia(valorInicial)

   Escreva("Digite a taxa de juros (em porcentagem): ")
   Leia(taxaJuros)

   Escreva("Digite o tempo em meses: ")
   Leia(tempo)

   // Converte a taxa de juros para decimal
   taxaJuros <- taxaJuros / 100

   // Calcula o montante (valor final) com juros compostos
   montante <- valorInicial
   Para contador de 1 ate tempo faca
      montante <- montante * (1 + taxaJuros)
   FimPara

   // Exibe o resultado
   Escreva("O montante com juros compostos é: ", montante)
FimAlgoritmo




