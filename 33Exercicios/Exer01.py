# 01) Faça uma função que receba um valor que é o valor pago, um segundo valor que é o preço do produto e
# retorne o troco a ser dado.
valorPago = float((input("Digite o valor com que se paga ? ")))
precoProduto = float((input("Digite o preço do produto ? ")))

if precoProduto > valorPago:
    print("Valor para inferior ao preço do produto")
else:
    troco = valorPago - precoProduto
    print("Seu troco : ", troco)
