#    02) Faça um programa que receba o valor do quilo de um produto e a quantidade de quilos do produto
#    consumida calculando o valor final a ser pago.

valorKilo = float(input("Digite o preço do quilo do produto...: "))
qtdKilos = float(input("Digite a quantidade de kilos compras.: "))
valorPagar = valorKilo * qtdKilos

print("Valor a ser pago.....................: %.2f " % valorPagar)

