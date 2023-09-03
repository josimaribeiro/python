salarioMinimo = float(input("Qual o valor do salario minimo hoje : "))
nome = input("Digite seu nome :  ")
salarioBruto = float(input("Valor do salario bruto : "))


if salarioBruto < salarioMinimo:
    valorDesconto = 2.00
elif salarioBruto == salarioMinimo:
    valorDesconto = salarioBruto * 5 / 100
else:
    valorDesconto = salarioBruto * 8 / 100
salarioLiquido = salarioBruto - valorDesconto

print("Valor do desconto : ", valorDesconto)
print("Valor do salario liquido : ", salarioLiquido)
