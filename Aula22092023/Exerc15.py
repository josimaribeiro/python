"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o
 Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.

Para as remunerações que são vinculadas ao salário mínimo, 
o valor diário será equivalente a R$ 40,40 e o valor por hora será de R$ 5,51.


"""
valor_hora = float(input("Digite o valor que você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

# Calcula o salário bruto
salario_bruto = valor_hora * horas_trabalhadas

# Calcula os descontos
ir = 0.11 * salario_bruto
inss = 0.08 * salario_bruto
sindicato = 0.05 * salario_bruto

# Calcula o salário líquido
salario_liquido = salario_bruto - (ir + inss + sindicato)

# Exibe os resultados
print(f"Salário Bruto......................: R$ {salario_bruto:.2f}")
print(f"Desconto do Imposto de Renda (11%).: R$ {ir:.2f}")
print(f"Desconto do INSS (8%)..............: R$ {inss:.2f}")
print(f"Desconto do Sindicato (5%).........: R$ {sindicato:.2f}")
print(f"Salário Líquido....................: R$ {salario_liquido:.2f}")
